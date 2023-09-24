import subprocess
from src import config as cfg

def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'The file "{file_name}" has been successfully saved.')
    except Exception as e:
        print(f'An error occurred while writing the file: {e}')
    return file_name

def delete_file(file_name):
    try:
        import os
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f'The file "{file_name}" has been successfully deleted.')
        else:
            print(f'The file "{file_name}" does not exist.')
    except Exception as e:
        print(f'An error occurred while deleting the file: {e}')
import requests
import os

def download_discord_images_from_string(input_string, save_folder,filename):
    """
    This function searches for links in the input_string that start with "https://cdn.discordapp.com"
    and end with ".png". It then downloads the images and saves them to the specified folder.

    Args:
        input_string (str): The input string to search for links in.
        save_folder (str): The folder where the downloaded images will be saved.

    Returns:
        list: A list of downloaded image file paths.
    """
    # Create the save folder if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Split the input string into words and check for links
    words = input_string.split()
    downloaded_images = []

    for word in words:
        if word.startswith("https://cdn.discordapp.com") and word.endswith(".png"):
            try:
                # Generate a unique filename for each image based on its URL
                image_name = os.path.basename(filename)
                image_path = os.path.join(save_folder, image_name)

                # Download the image and save it
                response = requests.get(word)
                if response.status_code == 200:
                    with open(image_path, 'wb') as image_file:
                        image_file.write(response.content)
                    downloaded_images.append(image_path)
                else:
                    print(f"Failed to download image from {word}")

            except Exception as e:
                print(f"Error downloading image from {word}: {e}")

    return downloaded_images

def startGenrateImg(prompt,mode,name):
    try:
        # Creating a list of command-line arguments
        command =f"npx ts-node ./src/apiMidjourney.ts {write_to_file('promptTmp.txt', prompt)}" 

        # Running the TypeScript process with arguments and capturing the output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        
        # Displaying standard output (stdout)
        print(result.stdout)
        download_discord_images_from_string(result.stdout, f"{cfg.RESOURCES}/{mode}/",f"{name}.png")

    except subprocess.CalledProcessError as e:
        print("Error while executing the command:")
        print(e.stderr)
    delete_file("promptTmp.txt")

def generateBeastPrompt(beast):
    result=f"""Draw a creature named {beast["name"]}. Its description is: {beast["description"]}.
Let the dominant colors be: {beast["color"]}.
The elements of the creature are: {beast["element"]}. --fast"""
    return result

def generatePlacePrompt():
    result=""
    return result