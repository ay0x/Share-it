# yourapp/uploadhandler.py
from django.core.files.uploadhandler import TemporaryFileUploadHandler, MemoryFileUploadHandler
from django.core.exceptions import SuspiciousOperation
import time

class CustomUploadHandler(TemporaryFileUploadHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth_upload_speed_limit = 5 * 1024 * 1024  # 5 MB/s for authenticated users
        self.auth_max_file_size = 50 * 1024 * 1024  # 50MB for authenticated users
        
        self.anon_upload_speed_limit = 1 * 1024 * 1024  # 1 MB/s for unauthenticated users
        self.anon_max_file_size = 10 * 1024 * 1024  # 300MB for unauthenticated users
        
        self.start_time = time.time()
        self.total_upload_size = 0

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding):
        user = self.request.user
        if user.is_authenticated:
            self.upload_speed_limit = self.auth_upload_speed_limit
            self.max_file_size = self.auth_max_file_size
        else:
            self.upload_speed_limit = self.anon_upload_speed_limit
            self.max_file_size = self.anon_max_file_size
        
        if content_length < self.max_file_size:
            return MemoryFileUploadHandler().handle_raw_input(input_data, META, content_length, boundary, encoding)
        else:
            return super().handle_raw_input(input_data, META, content_length, boundary, encoding)

    def receive_data_chunk(self, raw_data, start):
        self.total_upload_size += len(raw_data)
        
        # Check file size limit
        if self.total_upload_size > self.max_file_size:
            raise SuspiciousOperation("File size exceeds limit.")

        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time
        
        # Calculate current upload speed
        if elapsed_time > 0:
            current_speed = self.total_upload_size / elapsed_time
            if current_speed > self.upload_speed_limit:
                time.sleep((self.total_upload_size / self.upload_speed_limit) - elapsed_time)
        
        return raw_data

    def file_complete(self, file_size):
        return None

    def new_file(self, field_name, file_name, content_type, content_length, charset=None, content_type_extra=None):
        self.total_upload_size = 0
        self.start_time = time.time()
        super().new_file(field_name, file_name, content_type, content_length, charset, content_type_extra)

    def set_request(self, request):
        self.request = request
