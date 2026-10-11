from .BaseController import BaseController 
from models import ResponseSignal
from .ProjectController import ProjectController
import re
import os
class DataController(BaseController):
    
    def __init__(self):

        super().__init__()

    def validate_uploaded_file(self, file):
        self.size_scale = 1024 * 1024  # 1 MB in bytes

        # Validate the file properties
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        # Check the file size
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * self.size_scale:
            return False , ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        # Reset the file pointer after reading
        return True , ResponseSignal.FILE_VALIDATION_SUCCESS.value


    def generate_uninque_filepath(self, orig_file_name: str, project_id: str):
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_filename = self.get_clean_file_name(orig_file_name=orig_file_name)
        new_file_path = os.path.join(
            project_path, 
            random_key + "_" + cleaned_filename
        )

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path, 
                random_key + "_" + cleaned_filename
            )
        return new_file_path ,random_key + "_" + cleaned_filename


    def get_clean_file_name(self, orig_file_name: str):
        # Remove any special characters excet _ and .
        cleaned_filename = re.sub(r'[^\w .]', '', orig_file_name.strip())

        # replace spaces with underscores
        cleaned_filename = cleaned_filename.replace(' ', '_')
        return cleaned_filename


