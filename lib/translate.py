import requests
from lib.papagopy.papagopy import Papagopy
import io
from PIL import Image
import os.path


def translate_image(server_base_url, image_path, output_path):
    
    r = requests.post(f'{server_base_url}/manual-translate', files={'file':open(image_path, 'rb').read()})
    j = r.json()
    tr = j['trans_result']
    src_text = [res['s'] for res in tr]

    p = Papagopy()
    trans_text = p.translate('\n'.join(src_text), 'ko').split('\n')


    a = []
    for s, t in zip(src_text, trans_text):
        a.append({'s': s, 't': t})
    j['trans_result'] = a

    r2 = requests.post(f'{server_base_url}/post-translation-result', json=j)

    j = r2.json()
    status = j['status']
    if status == 'successful':
        taskId = j['task_id']
        transed_img_url = f'{server_base_url}/result/{taskId}'

        Image.open(
            io.BytesIO(
                requests.get(url=transed_img_url).content
            )
        ).save(output_path)

        return output_path

    else:
        return None