import requests
from pathlib import Path

"""
    The function download_to_local is designed to download a 
    file from a specified URL and save it to a specified path on your local file system.
"""
def download_to_local(url:str,out_path:Path,parent_mkdir:bool=True):

    # checks if the out_path provided is a valid Path object (from pathlib)
    if not isinstance(out_path,Path):
        raise ValueError(f"{out_path} must be a valid pathlib. Path object")

    if parent_mkdir:
        out_path.parent.mkdir(parents=True,exist_ok=True)
    
    
    try:
        # download the content from the url
        # Sends an HTTP GET request to the URL to fetch the content
        response=requests.get(url) 

        # raise exception if HTTP code indicates an error 404/500
        response.raise_for_status()

        # save to a file: write file in a binary mode to prevent any newline conversions
        out_path.write_bytes(response.content)

        return True
    except request.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False
        