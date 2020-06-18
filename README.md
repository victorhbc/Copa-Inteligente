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
    
Crie o arquivo database/credentials.json e adicione suas informações de credenciais do firebase

No aplicativo **IP Webcam**:
1. Clique em *Start server*

![](https://lh3.googleusercontent.com/pw/ACtC-3dmOvtzyDlZJPY-5PkV_lIAb4ues2--CWess1rNA4wEb9rMtrWPbDgwkp33TrXC3AFkRy5vPVah1Jiocs26vh6HrOU_a7nUdKn5mK14bWMua-YXb2fTHQxG70Mg2Iq9QNUBWc1fUOLgKJ7idOdV72XImQ=w627-h937-no?authuser=0)

2.Copie o endereço de IPv4 na [URL] linha 28 exec.py

    url = '[URL]/shot.jpg'

Execute o comando 

    py exec.py

siga para a branch dashboard
