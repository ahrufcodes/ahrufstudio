import openai

# Set up your OpenAI API key
openai.api_key = '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'

def refine_prompt_with_gpt(user_prompt):
    refined_prompt = f"Refine this prompt for DALL-E: '{user_prompt}'"
    return refined_prompt

def generate_image_with_dalle(refined_prompt):
    try:
        response = openai.Image.create(
            prompt=refined_prompt,
            n=1,
            size="1024x1024"
        )
        return response
    except Exception as e:
        print(f"Error generating image with DALL-E: {e}")
        return None
    
def save_image(image_url, filename):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image saved as {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")


def main():
    user_prompt = input("Please describe the idea for your logo: ")
    refined_prompt = refine_prompt_with_gpt(user_prompt)

    image_response = generate_image_with_dalle(refined_prompt)

    if image_response:
        # Assuming the response contains an image URL
        image_url = image_response['data'][0]['url']  # Adjust based on response structure
        print(f"Image generated: {image_url}")
        # Add logic to download and save the image if necessary
    else:
        print("Failed to generate an image.")

if __name__ == "__main__":
    main()
