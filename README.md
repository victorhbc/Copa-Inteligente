# python

Para executar o projeto é necessário PC ou Raspberry Pi 3 || 4 com Python 3.7 e de uma câmera IP ou um celular android com o app [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=pt_BR) para emular a mesma

Instale os seguintes pacotes

    $pip install urllib.request python-firebase pprint boto3 pyscreenshot

Instale o AWS CLI

    $pip install awscli

Crie um perfil de IAM no AWS com acesso ao rekognition ou administrador coloque as credenciais geradas após o seguinte comando

    $aws configure
    AWS Access Key ID: [YOUR_ACESS_KEY_ID]
    AWS Secret Access Key: [YOUR_SECRET_KEY]
    Default region name: [region]
    Default output format: json
    
No arquivo database/credentials.json adicione suas informações de credenciais

No aplicativo **IP Webcam**:
1. Clique em *Start server*

![](https://lh3.googleusercontent.com/pw/ACtC-3dmOvtzyDlZJPY-5PkV_lIAb4ues2--CWess1rNA4wEb9rMtrWPbDgwkp33TrXC3AFkRy5vPVah1Jiocs26vh6HrOU_a7nUdKn5mK14bWMua-YXb2fTHQxG70Mg2Iq9QNUBWc1fUOLgKJ7idOdV72XImQ=w627-h937-no?authuser=0)
	
2. Copie o endereço de IPv4

![](https://lh3.googleusercontent.com/nG5EiVIXqyJHfIEKveVd6XapU3xC32ngpd6V9_25PEWjqQaiAfzFyGPvXL7_83EONqmTggHcDsZyp3G604TsY7CUqChlVVln9kVE0hmRTxaIS6qYQokaA_mVA8IS4DVKRva--_Z7tj_N1HryYrSaLMwChDMY-gQwwNutKnusRaH-xuYhUcKB43jphzr0OubF-B2desrpUcFD4FS6WmgEXJUlHhOplkA251Etzpvs3Tr6rN2PHKNYNw93SJZh1T4Ci02JSYNkHq_-FSwYUbUx9UKHOwHKuv-sZTXcvfgPGJHqJiwDVvMWHbKCbJPVW1CwC-rOg9xuszj8TL6jdA5b9hWmHUclRnr9A42im-VSPyJybwv7r5jknVIAxAY_RcefkfIvk-eci9jnXImvp5Y9HFkihvOgbD4ECFo9zhO_Xa7OsbNUAFbbe-hP1sczA-kFeHmWHokaE_bZapMIYk6O5csvcqa6Q-j2IwedgPPHn92Xz7UX6rKX0TF57VP_CfNNmjF52w9Qz0_CkM-HgPfHDpVyV6Gts2coB-fwSLulcjOjiqzRlhl3_9jQZtS9m7gFFbHxE4WWVlNDieLDd1gtFZ2X3dyn0fpzmzOxcXjMPDFCCmZHbl3KgPlgn5tX0lpZ0HaU3_P4K_4VP5vHfAG-zng_BZDhQxhA8kRO5xdnNZmaBuWkSa_W5saAUh9rFLrRlAUMxWw=s1121-w1121-h263-no?authuser=0)

Execute o comando 

    py exec.py

siga para a branch dashboard
