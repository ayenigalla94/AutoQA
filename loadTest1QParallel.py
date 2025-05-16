import requests
import json
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "https://parth-m722bnfy-swedencentral.services.ai.azure.com/models/chat/completions?api-version=2024-05-01-preview"
headers = {
    'Content-Type': 'application/json',
    'api-key': '8IXpoVgbHXlSWiDQVN3uji1luZZMp5VuSPbcUPHFcVcsLqIAzUqaJQQJ99BBACfhMk5XJ3w3AAAAACOGlcHJ'
}

def create_payload():
    return json.dumps({
        "messages": [
            {"role": "system", "content": '''Answer the following questions based on the interaction between a call-center agent and a customer.
Ensure the output conforms to the JSON format below:
{
    "Question #": "[Question Number]",
    "Answer": "[Yes/No]"
}'''},
            {"role": "user", "content": '''<|eot_id|>
<|start_header_id|>user<|end_header_id|>


    Question 1: Determine whether the associate used explicit empathetic language to acknowledge the customer's situation, feelings, or concerns.\nIf the agent demonstrated empathy by using phrases such as 'I understand how frustrating that must be,' 'I can see why that would be upsetting,' or 'That sounds like a difficult situation,' respond with 'Yes' and provide the exact wording.\nIf the customer expressed frustration, concern, or distress but the associate did not respond with empathetic language, respond with 'No' and note the missed opportunity.\nIf the transcript does not indicate a situation where empathy was needed (e.g., a routine inquiry or neutral discussion), respond with 'NA' to indicate empathy was not required in the interaction.\nEnsure that generic conversational fillers like 'I hear you' or 'I understand' are only counted if they are followed by a meaningful empathetic statement.\n \nINTERACTION(4.5minute call):\nSpeaker 0: Thank you for calling American Eagle. My name is Melissa. Can I help you today? Hi. Good afternoon.\n \nMy name is May. Today, I just saw my online, I checked my packages, but I didn't receive my, packages. So, I just wanna call you, ask what happened. But but I I online check delivered. I'm sorry.\n \nYou said that I understand your concern. I'm sorry. Go ahead. I'm sorry. My English is nowhere, so I cannot explain very clear.\n \nI just want want to say I checked the, online, all the all the detail. Detail is say shipped, but I didn't receive. I will be happy to check-in today for you. Can I have your order number, please? Yes.\n \nOrder number is, 0162972207. Can I have your full name and full billing address, please? Adrienne Wright. And your billing address? I don't understand.\n \nSorry. Okay. What is your address? Oh, address. 2, 204 North Nicholson Avenue, Monterey Park, California.\n \nApartment numb what is your apartment number? Apartment Number is B. And your ZIP code? What? Your ZIP code.\n \nZIP code is 91755. Thank you. Let me check it for you. I see that we ship it on the twenty eighth. Let me check it for you.\n \nOne moment, please. Thank you. You're welcome, ma'am. It says that the package was delivered on Saturday at 11:43. Did you check with your neighbor or around the house?\n \nI checked, but nobody answers. So I don't know, if your company shipped, deliver or post office deliver. I don't know. I just went to the, post office, ask I give the tracking number. They say, oh, I we don't know.\n \nThey just, delivered already. I say, can you, can you check who is deliver for my packages? They say, I don't know. They they they cannot give me the the the answer. They let me they say you can ask, call the American Eagle company.\n \nAsk. So that's why I told you. Sorry. Okay. I understand that, and we are truly sorry for that.\n \nSince the order shows delivered on the second on Saturday, we'll have to provide them seventy two hours to correct any issue with the delivery. And the seventy two hours ends tomorrow. So if you don't receive your package by tomorrow, you can call us back. Okay? Oh, okay.\n \nThank you. You're welcome. Is there anything else I can do for you today? No. Thank you for calling American Eagle.
    Answer the following in the format provided:
    {
        "Question #": "1",
        "Answer": "[Yes/No]",
    }
	<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>'''}
        ],
        "model": "DeepSeek-V3-0324",
        "max_tokens": 10000
    })

def send_request(index):
    sent_time = datetime.now()
    print(f"[{sent_time.strftime('%H:%M:%S.%f')[:-3]}] Request {index} sent")

    start = time.time()
    try:
        response = requests.post(url, headers=headers, data=create_payload())
        end = time.time()

        received_time = datetime.now()
        elapsed = round(end - start, 2)

        print(f"[{received_time.strftime('%H:%M:%S.%f')[:-3]}] Response {index} received (Took {elapsed} seconds)")

        return {
            "request_index": index,
            "sent_time": sent_time.isoformat(),
            "received_time": received_time.isoformat(),
            "duration_seconds": elapsed,
            "response_text": response.text,
            "status_code": response.status_code
        }
    except Exception as e:
        return {
            "request_index": index,
            "sent_time": sent_time.isoformat(),
            "error": str(e)
        }

def run_batch(indices, max_workers):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(send_request, idx) for idx in indices]
        for future in as_completed(futures):
            results.append(future.result())
    return results

def make_staggered_requests(total_requests=500, first_batch_size=300, delay_between_batches=0.5, max_workers=100):
    first_indices = list(range(1, first_batch_size + 1))
    second_indices = list(range(first_batch_size + 1, total_requests + 1))
    third_indices = list(range(first_batch_size + 1, total_requests + 1))

    print(f"Sending first batch of {len(first_indices)} requests...")
    batch1 = run_batch(first_indices, max_workers)

    print(f"Waiting {delay_between_batches} seconds before sending second batch...")
    time.sleep(delay_between_batches)

    print(f"Sending second batch of {len(second_indices)} requests...")
    batch2 = run_batch(second_indices, max_workers)

    print(f"Waiting {delay_between_batches} seconds before sending third batch...")
    time.sleep(delay_between_batches)

    print(f"Sending second batch of {len(second_indices)} requests...")
    batch3 = run_batch(third_indices, max_workers)

    return batch1 + batch2 + batch3

# Run staggered parallel requests
responses = make_staggered_requests(total_requests=1000, first_batch_size=300, delay_between_batches=60, max_workers=300)

# Save all responses to a JSON file
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(responses, f, indent=2)

print("\n All responses saved to results.json")