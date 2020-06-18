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

![](https://lh3.googleusercontent.com/pw/ACtC-3dmOvtzyDlZJPY-5PkV_lIAb4ues2--CWess1rNA4wEb9rMtrWPbDgwkp33TrXC3AFkRy5vPVah1Jiocs26vh6HrOU_a7nUdKn5mK14bWMua-YXb2fTHQxG70Mg2Iq9QNUBWc1fUOLgKJ7idOdV72XImQ=w627-h937-no?authuser=0 =250x)
	
2. Copie o endereço de IPv4
![](https://lh3.googleusercontent.com/9YOTYhYidh_tJd3BrBEatA8muZMbIU1BUpPUnigeNJVabbKTzFafk7zBJZfeteaw4d2e_jMFu9zyT1j2r7hCFvHFSWE_DZXkbAGPMjXPAClzdJHX55ciyLwfmQj70QIoiQ4yvvnqzlrf6Pl_1TtOpzIEkWADnC1yqWiBoBc1Kkydll1qhhx8JV-oWauRld5VocmdFWzOeqp39Hdc0gUtdwvH9BdG52W1kc4Ek35IdO5FF7eqHARsICY0rYOxN9AUn1hWdS3yGk0B6ZVcOyxLMjHNX6TjklYn6aG5vJDtSSWotbIRydTYLGoeZx6l0gMCCs4s7hqbl771hzL5O-aRMypxac6oWGkDBACBESXNEo44sBg5P7rhvb44OLqFot0ral3_wZUml-4EmNL2Q3deVeZjSTxK0xYHWAJkebxloNPjzt6a5J3t6cHefKcvjXJ-ukRp1mCuBxEjjoImYPCN0LzgPJifj1G6JDFmVdRcG8OToOOd1bPLONgQ45UeGRaEiVLbIR5DnfqJ3TV9IZ1CbEgEIg59TPmDy3dbOFOJr78gTb332droIgLYbSfpAAIq8R6MC4AMj8cdya0JKahj2mRzkeh8JUJLpvuics5eKEBCwW41ouDJ43v2H5MtUqw-eJJ1AUb6IUzD3pXSlMibAyD28n5RwY9kyIH1oaS9TDQMHowH53ZP_PtUuB9dhw=w1121-h263-no?authuser=0 =250x)

Execute o comando 

    py exec.py

siga para a branch dashboard
