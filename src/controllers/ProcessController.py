# import os
# from .BaseController import BaseController
# from .ProjectController import ProjectController
# from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from models import ProcessingEnum

# import json
# from langchain_core.documents import Document
# from langchain_text_splitters import RecursiveJsonSplitter

# class ProcessController(BaseController):

#     def __init__(self, project_id: str):
#         super().__init__()

#         self.prject_id = project_id
#         self.project_path = ProjectController().get_project_path(project_id=project_id)


#     def get_file_extension(self, file_id: str) :
#        return os.path.splitext(file_id)[-1]


#     def get_file_loader(self, file_id: str):
#         file_extension = self.get_file_extension(file_id=file_id)
#         file_path = os.path.join(
#             self.project_path,
#             file_id
#         )

#         if file_extension == ProcessingEnum.PDF.value:
#             return PyMuPDFLoader(file_path)
        
#         if file_extension == ProcessingEnum.TXT.value:
#             return TextLoader(file_path, encoding="utf-8")

#         # if file_extension == ProcessingEnum.JSON.value:
#         #     with open(file_path, "r", encoding="utf-8") as f:
#         #         return json.load(f)
        
#         return None



#     def get_file_content(self, file_id: str):

#         loader = self.get_file_loader(file_id=file_id)  
#         if loader is None:
#             return None

#         if isinstance(loader, (dict, list)):
#              return loader

#         return loader.load() 


#     def process_file_content(self,file_content: list, file_id: str, chunk_size: int = 100, overlap_size: int = 20):
#         content = self.get_file_content(file_id=file_id)


#         text_splitter = RecursiveCharacterTextSplitter(
#             chunk_size=chunk_size,
#             chunk_overlap=overlap_size,
#             length_function=len
#         )
#         file_content_text = [
#             rec.page_content 
#             for rec in file_content
#         ]

#         file_content_metadata = [
#                     rec.metadata
#                     for rec in file_content
#                 ]

#         chunks = text_splitter.create_documents(
#             file_content_text,
#             metadatas = file_content_metadata
#         )
#         return chunks

#     # def process_file_content(
#     #     self,
#     #     file_id: str,
#     #     chunk_size: int = 100,
#     #     overlap_size: int = 20
#     # ):
#     #     file_content = self.get_file_content(file_id=file_id)

#     #     if not file_content:
#     #         return []

#     #     # JSON processing
#     #     if isinstance(file_content, (dict, list)):
#     #         # Convert Document objects to plain dictionaries if needed
#     #         if isinstance(file_content, list) and file_content and isinstance(file_content[0], Document):
#     #             file_content = [
#     #                 json.loads(doc.page_content)
#     #                 for doc in file_content
#     #             ]

#     #         splitter = RecursiveJsonSplitter(max_chunk_size=chunk_size)

#     #         json_chunks = splitter.split_json(
#     #             json_data=file_content,
#     #             convert_lists=True
#     #         )
#     #         return [
#     #             Document(
#     #                 page_content=json.dumps(
#     #                     chunk,
#     #                     ensure_ascii=False
#     #                 ),
#     #                 metadata={
#     #                     "file_id": file_id,
#     #                     "source": file_id,
#     #                     "chunk_index": index
#     #                 }
#     #             )
#     #             for index, chunk in enumerate(json_chunks)
#     #         ]

#     #     # PDF and TXT processing
#     #     text_splitter = RecursiveCharacterTextSplitter(
#     #         chunk_size=chunk_size,
#     #         chunk_overlap=overlap_size,
#     #         length_function=len
#     #     )

#     #     file_content_text = [
#     #         rec.page_content
#     #         for rec in file_content
#     #     ]

#     #     file_content_metadata = [
#     #         rec.metadata
#     #         for rec in file_content
#     #     ]

#     #     return text_splitter.create_documents(
#     #         file_content_text,
#     #         metadatas=file_content_metadata
#     #     )   
            















import os

from .BaseController import BaseController
from .ProjectController import ProjectController

from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from models import ProcessingEnum


class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.prject_id = project_id
        self.project_path = ProjectController().get_project_path(
            project_id=project_id
        )

    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1]

    def get_file_loader(self, file_id: str):
        file_extension = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(self.project_path, file_id)

        if file_extension == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)

        if file_extension == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding="utf-8")

        return None

    def get_file_content(self, file_id: str):
        loader = self.get_file_loader(file_id=file_id)

        if loader is None:
            return None

        return loader.load()

    def process_file_content(
        self,
        file_id: str,
        chunk_size: int = 100,
        overlap_size: int = 20
    ):
        file_content = self.get_file_content(file_id=file_id)

        if not file_content:
            return []

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len
        )

        file_content_text = [
            record.page_content for record in file_content
        ]

        file_content_metadata = [
            record.metadata for record in file_content
        ]

        return text_splitter.create_documents(
            file_content_text,
            metadatas=file_content_metadata
        )