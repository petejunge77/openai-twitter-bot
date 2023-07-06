
import http.client
import json
import time
import openai 




while True:
    import openai
    import os 

    openai.api_key = "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"
    # openai.api_key = os.getenv("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")

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="tell a dad joke. before you tell it, say something like hey buddy. before you say the joke state 'Dad joke of the day:' then say the joke.",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    content = response.choices[0].text
    print('before')
    print(content)
    print('after')
    print(response)

    conn = http.client.HTTPSConnection("api.twitter.com")
    payload = json.dumps({
    "text": str(content),
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'OAuth oauth_consumer_key="b6n6yF9EvTE18M1iZrAO13osb",oauth_token="1666204112558383134-D0i4XHfXf8MyIhnzfavo2Lcnt67UBt",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1688613466",oauth_nonce="zsIPeAExSLk",oauth_version="1.0",oauth_callback="twitter.com",oauth_signature="41zcsBLC3daQy9ZFesmb7RRo3WY%3D"'
    }
    conn.request("POST", "/2/tweets", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    time.sleep(86400)