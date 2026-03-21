from google import genai


client = genai.Client(api_key="YOUR_API_KEY_HERE")


with open(r'C:\Users\Puskar Mishra\OneDrive\Desktop\Puskar09\puskar09\SCRIPTS\sample_resume.txt', 'r') as f:
    resume = f.read()



# 3. Create the prompt
prompt = f"""
You are an expert tech recruiter in Bengaluru hiring for an AI startup. 
Read the following resume and give it a brutally honest score out of 10. 
Then, provide 2 quick bullet points on how to improve it.

Here is the resume:
{resume}
"""

print("Sending resume to the AI using the upgraded SDK... Please wait...")


response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

# 5. Print the analysis
print("\n--- AI RECRUITER ANALYSIS ---")
print(response.text)