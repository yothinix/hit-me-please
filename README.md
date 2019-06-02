# Delivering Quality Software from Scratch

[![CircleCI](https://circleci.com/gh/yothinix/hit-me-please.svg?style=svg)](https://circleci.com/gh/yothinix/hit-me-please)

## TL;DR

### Hit Me, Please!

CI/CD Wordshop @ Pronto


## Pre-requirement

- GCP Account
- GitHub Account
- Docker Hub Account

## Project

วันนี้เราจะทำ Landing page ชื่อ Hit Me! มีฟอร์มกรอก Name, Email, Phone (Optional) และปุ่ม Submit

## Intro

ทำพวก TDD, ATDD, Infra as Code, CI/CD แล้วจะช่วยลดความเสี่ยง

## Challenges in Software Development

การพัฒนาซอฟท์แวร์ process มันมาจากวิศวโยธาตั้งแต่ ออกแบบ ยันก่อสร้าง แต่เอามาใช้กับ Software ไม่ได้เพราะเราไม่เห็นว่าเราอยากได้ software แบบไหน Ideally เลยเนี่ย Waterfall เป็นโมเดลที่ดีมาก ถ้า requirement ไม่เปลี่ยน

แต่ Software ปัจจุบันมันไปเร็วมากมีเคสที่ไปเร็วไม่ทันอย่าง Nokia แล้วถ้าเรา move fast ไม่พอเราจะโดน disrupt การมี DevOps ทำให้ change failure rate ต่ำลง, เวลา commit → deploy เร็วขึ้น, deployment ถี่ขึ้นมากๆ และใช้เวลาพัฒนา feature ได้มากขึ้น เหมือนจะง่าย แต่สิ่งที่ยากคือ Maintain พวกนี้ให้อยู่ต่อไป

DevOps ไม่ควรแยกเป็น Silo อยู่ตรงกลางระหว่าง Dev กับ Ops

> DevOps เป็นเรื่องของคนและการแชร์ประสบการณ์เป็นหลัก ไม่เน้น Tools

## Shu Ha Ri

Shu — ทำตาม แต่คิดไปด้วย

Ha — ถ้าเราฝึกฝนจนชำนานแล้ว ออกไปหา Master คนอื่นบ้าง

Ri — เรามี Knowledge ของเรา สามารถประยุกต์กับอะไรก็ได้

---

# Practice to release quality software

> Why Software sucks?

- คนใช้ไม่ได้อยากได้ Software แต่คนใช้อยากแก้ปัญหาซักอย่างนึง ถ้าเค้าแก้ปัญหาได้โดยไม่ต้องใช้ Software ตัว Software ก็ไม่จำเป็น
- ถ้าทำ Software มาแล้วไม่มีใครใช้ แปลว่า Software นั้นห่วยในเชิง Business
- คำถามนี้เป็นชื่อหนังสือด้วย [http://www.whysoftwaresucks.com/](http://www.whysoftwaresucks.com/)

## ATDD — Acceptance test driven development

- อันนี้เป็นมุมมอง feature จากมุมมองที่ลูกค้าต้องการ
- The Loop: Test → Code → Refactor
    - Test: Collect requirement
    - Code: Implement
    - Refactor: Improve
- Requirement ตรงนี้จะค่อนข้าง high level

## TDD — Test Driven Development

- The Small Loop: Test → Code → Refactor
- อยู่ข้างใน Code ของ ATDD

หั่นฟีเจอร์ ให้เรา slice ไปแต่ต้อง work

> เวลาเราจะ release software เราต้อง Incremental release working software

> เวลาทำโปรเจ็ค level สำคัญ ชั้นบนสุดไว้เก็บ configuration พวก application จะอยู่ใน folder ย่อยๆ

## Cypress

- เก็บไว้ใน folder tests

    mkdir tests && cd tests
    yarn init
    yarn install --dev cypress

> Commit ควรจะมีแค่หนึ่งอย่าง ควรเป็นแค่ step เล็กๆ

> Commit message ให้เริ่มด้วย Capitalize Verb

- รัน cypress

    # cli
    $ node_modules/.bin/cypress open

    # package.json
    "scripts": {
    	"cypress": "cypress"
    }
    $ yarn cypress open

- Cypress ทำให้ high level ไว้ก่อน อะไรที่มันซับซ้อนก็แยกไปเป็น command
- บางที่คิดว่า cy มันอ่านยากไปเลยใช้ const user = cy แทน
- พอได้ acceptance แล้วเอา flow นี้ไปคุยกับ PO / User ได้ว่า flow นี้โอเคมั้ย ถ้าโอเคก็เริ่ม implement ได้เลย

> เราไม่ commit สิ่งที่ failed

## Django

- สร้าง virtualenv ก่อน

    $ python -m venv ENV
    $ source ENV/bin/activate

- Install Django

    $ pip install django
    $ pip freeze > requirements.txt

- start Django project

    $ python -m django startproject hit_me_please
    # กลับไปดูว่าทำไมตรงนี้พังในเครื่องเราใช้ django-admin startproject ไม่ได้

- Django project structure

    $ tree -L 2 hit_me_please
    hit_me_please
    ├── hit_me_please
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py

    1 directory, 5 files

ก่อนจะเขียนโค้ดเรามาแบ่งฟีเจอร์เป็น Unit ย่อยๆ ก่อน เราทำได้หลายแบบเลือกอันไหนก่อนก็ได้

- ทำหน้าเว็บก่อนก็ได้
- ทำ model ต่อ database ก่อนก็ได้ (เราเลือกเริ่มที่ model)

> Django app นึงมี model ไม่ควรมีเกิน 3 model เพราะ code มันจะ complex ลึกไป และชื่อ app ควรเป็นพหูพจน์

- create app ไปทำที่ชั้น [manage.p](http://manage.py)y

    $ python manage.py startapp hitters

- Django app structure

    $ tree -L 2 hitters
    hitters
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

    1 directory, 7 files

### Create Model

- ทำ TDD เริ่มที่ tests.py
- Test suites จะใช้ความสามารถของ TestCase ก็ extend มันออกมา

    class HitterTest(TestCase):

- ทุก method ใน class ต้องมีตัวแปรไว้ represent ตัวมันเอง  Python ใช้คำว่า self

> TDD เขียนเทสให้ fail ก่อน แล้วเขียนโค้ดให้มันผ่าน (โง่ที่สุดและ minimum) แล้วค่อยกลับมา refactor

- เทส model ว่ามี field นั้นใน database ให้ retrieve ข้อมูลออกมาได้
- เทส field ไม่ต้องรู้ว่า มันคือ field ไหน

> เราไม่เขียนเทสไปเทส  Framework เราเขียนเทสเพื่อเทสโค้ดเรา

- สิ่งที่เราจะทำคือ สร้าง model สร้าง migrations รัน migrate ให้สร้าง Table ใน database

    $ python manage.py makemigrations
    $ python manage.py migrate

- เขียนเทส Admin ต้องเช็คก่อนว่า admin ของ model นี้มันถูก register แล้ว
- ลำดับการ import ของ Python / Django
    - Python Built-in
    - Django app / module
    - 3rd Parties module
    - local apps
- Runserver Django

    $ python manage.py runserver

- ไม่ว่าจะสร้าง project ที่ไหน Production, dev, local เราต้องสร้าง admin ซักคน

    $ python manage.py createsuperuser

> ถ้ามีโอกาสทำ Automate ตั้งแต่แรกให้ทำไปเลย เพราะถ้าทำทีหลังจะยากกว่าละ

### Create View

- ตอนเขียนเทสต้องจินตนาการว่า HTML มันจะเป็นยังไงก่อน
- ทุกแอพควรมี urls.py ของมันเอง
- เวลาเขียนเทสแบ่งเป็น 3 ส่วน
    - Given — เตรียมว่าจะเกิดอะไรก่อน
    - When — เมื่อเราทำอะไรบางอย่าง
    - Then — จะเกิดอะไรขึ้น
- ฟอร์มควรจะใส่ csrf token แต่จะเขียนเทสก่อนใส่

---

หลังจากนี้งานที่ทำจะกลับไปกลับมาจาก build pipeline

## Docker

- เวลาเราทำ docker เนี่ยเราจะ build application ขึ้นมาตัวนึงแล้วก็ Run
- เราจะไม่ทำใหม่ทั้งหมด จะใช้ของที่ชาวบ้านทำไว้อยู่แล้ว Python:image

    $ docker pull python:3.7-alpine

- บรรทัดแรกส่วนใหญ่จะบอกว่ามาจาก image ตัวไหน

    FROM scratch # อันนี้คือถ้าไม่มี image แม่
    FROM python:3.7-alpine

- พอ build เสร็จเราต้องคิดเลยว่าเราจะมี Django ในนี้ได้ไง
- Copy รับ 2 arguments

    COPY <source-on-host> <destination-on-docker-image>

- ย้ายตัวเองไปอยู่ directory นั้นใน image

    WORKDIR <directory>

- สั่ง run command ต่างๆ

    RUN <command>

- คำสั่ง build

    $ docker build -t hitme:v1 .
    # จะเลือก . คือ context ที่จะ build

- รัน application

    CMD # override ได้โดยการพิมพ์คำสั่งตามหลังตอน run
        # e.g. docker run -p 8000:8000 hitme:v1 ls
    ENTRYPOINT # override ตรง entrypoint แบบใช้ --entrypoint ตอนรันแทน

    docker run -p 8000:8000 hitme:v1

- Dockerhub จะมี format มันอยู่ในชื่อ image เช่น yothinix/imagename:version Docker จะได้รู้ว่าจะวิ่งเข้าไปที่ไหน ถ้าของ AWS จะเป็นชื่อ Registry ยาวๆ
- ถ้าจะ push เข้า Dockerhub ต้อง docker login ก่อน แล้วค่อย push ด้วยชื่อ image และ version

    $ docker login
    $ docker push yothinix/hitme:v1

## GCP — VM instance — Setting up Production instance

- private key ที่ generate มากากๆ บางครั้งก็ใช้ไม่ได้
- ลง docker  แบบง่ายๆ [https://get.docker.com/](https://get.docker.com/) มีแค่ 2 step

    $ curl -fsSL https://get.docker.com -o get-docker.sh
    $ sh get-docker.sh

- รัน container บน production

    $ docker run -p 80:8000 yothinix/hitme:v1
    # 80 คือเครื่อง 8000 คือ container

- Update  ALLOWED_HOST ใน Django แล้ว build / push ใหม่

    # local
    docker build -t yothinix/hitme:v2 .
    docker push yothinix/hitme:v2

    # server
    docker run -p 80:8000 yothinix/hitme:v2

## Docker compose instead of Docker run

- ไม่อยากรันแล้ว สร้าง docker-compose file
- ลง docker-compose ในเครื่อง production วิธีอยู่ที่ [https://github.com/docker/compose/releases](https://github.com/docker/compose/releases)

    curl -L https://github.com/docker/compose/releases/download/1.25.0-rc1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

- copy docker-compose file ไป production
- ปกติบน production จะ make sure ก่อนว่ามี image ใช้

    docker-compose pull
    docker-compose up

## CircleCI

- เปลี่ยน Github เป็นชื่อตัวเอง แล้ว add project แล้วกด setup project
- 1 Workflow มีหลาย job | 1 Job มีหลาย Step
- run → command ต้อง activate virtualenv ทุกครั้ง เพราะมันแยกกัน

## (Automated) Deployment via CI

- Machine
- Code
- CI
- Tool (remote execution)

### Terraform

- ลงผ่าน brew ได้ง่ายๆ

    brew install terraform

- Command ที่ใช้บ่อย

    terraform init # ใช้แค่ครั้งแรก
    terraform plan # คล้ายๆ dry run
    terraform apply # เอา config เราไปรันใน cloud provider
    terraform destroy # ตามนั้น

สร้าง folder terraform ไว้ใน project

- ก่อนจะรัน terraform init ต้องมีไฟล์ main[.tf](http://terraform.tf) ก่อน

    $ terraform init

    Initializing the backend...

    Terraform has been successfully initialized!

    You may now begin working with Terraform. Try running "terraform plan" to see
    any changes that are required for your infrastructure. All Terraform commands
    should now work.

    If you ever set or change modules or backend configuration for Terraform,
    rerun this command to reinitialize your working directory. If you forget, other
    commands will detect it and remind you to do so if necessary.

- Documents [https://www.terraform.io/docs/index.html](https://www.terraform.io/docs/index.html) บางคำสั่งจะซ้ำกันต้องดู section
    - Provider เราใช้ที่ไหนก็ดูที่นั่น
    - เวลาสร้างเราจะดูใน Compute Engine เป็นหลัก ไม่ดู Data Source
    - Data Source เอาไว้ get information ต่างๆ
- Step แรกคือต้อง set provider ให้ terraform ก่อน

    provider "google" {
      credentials = "${file("account.json")}"
      project     = "my-project-id" # อันนี้ไปดูได้ที่ GCP Home -> Project Info -> Project ID
      region      = "asia-southeast1"
      zone        = "asia-southeast1-b"
    }

- ${file()} จะอ่าน content ของไฟล์
- สร้าง Credential ใน GCP
    - API & Services → Credentials → Create → Service Account Key
    - Service Account Name: `hitmeplease`
    - Select Service Account: `New Service Account`
    - Role: `Compute Admin`
    - Click `Create`
- เอาไฟล์ JSON ที่ได้ มาไว้ที่เดียวกับ terraform แล้วเปลี่ยนชื่อเป็น `hitmebaby.json`
- Autocomplete zsh [https://github.com/hashicorp/terraform/tree/master/contrib/zsh-completion](https://github.com/hashicorp/terraform/tree/master/contrib/zsh-completion)
- เราจะเก็บแค่ [main.tf](http://main.tf) ส่วนพวก terraform.tfstate จะแชร์ไฟล์เก็บไว้ซักที่
- Configuration for create instance มีตัวอย่างอยู่ที่ [https://www.terraform.io/docs/providers/google/r/compute_instance.html#network_interface](https://www.terraform.io/docs/providers/google/r/compute_instance.html#network_interface)

    resource "google_compute_instance" "tf_instance" {
      name         = "tf-instance"
      machine_type = "n1-standard-1"

      boot_disk {
        initialize_params {
          image = "ubuntu-1804-bionic-v20190514"
          size  = 30
        }
      }

      metadata = {
        sshKeys = "hitme:${file("~/.ssh/hitme.pub")}"
      }

      network_interface {
        network       = "default"
        access_config {}
      }

      tags = ["my-web"]
    }

- ลง gcloud command line SDK [https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version)
    - โหลดมาแล้วแตก zip แล้วเอาไปไว้ที่ home
    - รัน `./google-cloud-sdk/install.sh`
    - รัน `./google-cloud-sdk/bin/gcloud init`
- วิธีดูชนิดเครื่อง

    $ gcloud compute machine-types list | grep asia-southeast1-b
    n1-standard-1    asia-southeast1-b          1     3.75
    n1-standard-16   asia-southeast1-b          16    60.00
    n1-standard-2    asia-southeast1-b          2     7.50
    n1-standard-32   asia-southeast1-b          32    120.00
    n1-standard-4    asia-southeast1-b          4     15.00
    n1-standard-64   asia-southeast1-b          64    240.00
    n1-standard-8    asia-southeast1-b          8     30.00
    n1-standard-96   asia-southeast1-b          96    360.00
    n1-ultramem-160  asia-southeast1-b          160   3844.00
    n1-ultramem-40   asia-southeast1-b          40    961.00
    n1-ultramem-80   asia-southeast1-b          80    1922.00

 แล้วก็จะ search หาเครื่องจาก zone ได้เช่น `asia-southeast1-b` จะได้ machine type เป็นโค้ดเช่น `n1-standard-1`

- วิธีหา boot disk

    $ gcloud compute images list | grep ubuntu
    ubuntu-1404-trusty-v20190514                          ubuntu-os-cloud    ubuntu-1404-lts                               READY
    ubuntu-1604-xenial-v20190530c                         ubuntu-os-cloud    ubuntu-1604-lts                               READY
    ubuntu-1804-bionic-v20190530                          ubuntu-os-cloud    ubuntu-1804-lts                               READY
    ubuntu-1810-cosmic-v20190530                          ubuntu-os-cloud    ubuntu-1810                                   READY
    ubuntu-1904-disco-v20190529                           ubuntu-os-cloud    ubuntu-1904                                   READY
    ubuntu-minimal-1604-xenial-v20190527                  ubuntu-os-cloud    ubuntu-minimal-1604-lts                       READY
    ubuntu-minimal-1804-bionic-v20190529                  ubuntu-os-cloud    ubuntu-minimal-1804-lts                       READY
    ubuntu-minimal-1810-cosmic-v20190529a                 ubuntu-os-cloud    ubuntu-minimal-1810                           READY
    ubuntu-minimal-1904-disco-v20190528                   ubuntu-os-cloud    ubuntu-minimal-1904                           READY

เราก็เลือก `ubuntu-1804-bionic-v20190530`

- verify config ว่าถูกรึเปล่า

    $ terraform plan

- เอา config  ไปสร้างเครื่องจริงๆ ผ่าน

    $ terraform apply

- ถ้าอยากได้ value อะไรก็ตามตอนสร้าง instance เสร็จ เช่นเอาไปใช้กับ Ansible ต่อ เช่น External IP

    output "ip" {
      value = "${google_compute_instance.tf_instance.network_interface.0.access_config.0.nat_ip}"
    }

- ลบเครื่องออกจาก known host

    ssh-keygen -R <HOST>

- `คำเตือน`: ถ้าจะ ssh เข้าเครื่องโดยไม่ใช่ key default (id_rsa) ต้องบอก ssh ว่าจะใช้ key ไหนด้วย

    ssh -i ~/.ssh/hitme hitme@<HOST>

- สร้าง terraform มากกว่า 1 เครื่องกับ config เดิมให้เพิ่ม count เข้าไป แต่ถ้ามี output ให้เพิ่ม .*.

    # เพิ่ม count 3 แปลว่าสร้าง 3 เครื่อง
    resource "google_compute_instance" "tf_instance" {
      name         = "tf-instance-${count.index}"
      machine_type = "n1-standard-1"
      count        = 3

    # ตรงชื่อเครื่องเพิ่ม .*. แปลว่าเอาทุกเครื่อง
    output "ip" {
      value = "${google_compute_instance.tf_instance.*.network_interface.0.access_config.0.nat_ip}"
    }

### Ansible

- File structure
    - Playbooks
        - Roles — e.g. Nginx, Docker
            - Tasks — e.g. Add ssh key, Install nginx, Install Docker
    - Inventory — Role of Server e.g. Web
    - group_vars — จะอ่านไฟล์ชื่อ all หรือตาม inventory name
- สร้าง folder ansible | สร้าง virtualenv แล้วลง ansible ผ่าน

    pip install ansible

- เทส ansible ใช้ได้ ต่อเครื่องตัวเองได้

    ansible localhost -a ls

- สร้าง inventory — สร้างไฟล์ ansible/hosts เสร็จแล้วเพิ่ม Inventory

    [web]
    12.34.56.78 ansible_python_interpreter=/usr/bin/python3 ansible_ssh_user=hitme ansible_ssh_private_key_file=~/.ssh/hitme

บางครั้งเครื่องปลายทางไม่ได้ลง Python3 ไว้ก็ต้องบอกให้ ansible รู้ด้วย

ต้องบอกคีย์ที่เราจะใช้เข้าเครื่องด้วยด้วย

- เทส Inventory ว่าเวิร์คแล้ว

    ansible -i hosts web -a ls

- แต่ถ้าเอา config ไปเก็บไว้ใน inventory มันก็จะรกมากๆ ก็เลยเอาพวก config พวกนี้ไปเก็บไว้ใน group_vars

    # ansible/group_vars/all
    ansible_python_interpreter: /usr/bin/python3
    ansible_ssh_user: hitme
    ansible_ssh_private_key_file: ~/.ssh/hitme

- สร้าง Playbook

    # ansible/provision.yml

    name: set up web server
      hosts: web
      roles:
        - docker

หมายความว่าจะ setup webserver ขึ้นมาที่ host web และให้ทำ role common กับ docker

- สร้าง Role

    $ tree -L 3
    .
    └── roles
        └── docker
            └── tasks
                └── main.yml

หน้าตาของ tasks ก็จะประมาณนี้

    - name: list directories and files
      command: "ls"

- รัน playbook

    $ ansible-playbook -v -i hosts provision.yml

- Ansible มี module ไว้ช่วยให้เราทำงานสะดวกๆ เช่น apt, service

> ถ้าใช้โมดูลได้ให้ใช้โมดูล แต่ถ้าใช้โมดูลไม่เป็น ให้ใช้ command ก็ได้

- รัน ansible-playbook แบบ custom extra-vars

    $ ansible-playbook -v -i hosts deploy.yml --extra-vars "project_path=/Users/man/projects/_class/hit-me-please username=hitme"

## Integrate Ansible with CircleCI

- ถ้าจะทำให้ circle CI build docker ได้ต้องใส่ setup_remote_docker จะทำให้เราใช้ docker build image ได้ด้วย

    steps:
      - setup_remote_docker

- เพิ่ม build docker image step ให้กับ circleCI

    - run:
        name: build & push image
        command: |
          docker build -t yothinix/hitme:live .
          docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
          docker push yothinix/hitme:live

ต้องไปแก้ Environment Variable ที่ CircleCI ด้วย เข้าไปตรง Project Settings → Build Settings → Environment Variable จากนั้นเพิ่ม Add Value

- Step deploy ใน circleci.yml

    - run:
        name: deploy
        command: |
          cd ansible
          ansible-playbook -v -i hosts deploy.yml --extra-vars "project_path=~/hitme username=circleci"

ต้องไปเพิ่ม SSH Permissions แล้ว Add SSH Key แล้วเอา Private Key มาแปะไว้ที่นี่ (Key ที่เอามาแปะบบน circleCI นี้ต้อง generate ใน Linux อันที่ generate  บน mac os ไม่เวิร์ค)

project_path อันนี้ตาม working_directory ข้างบน

`จังหวะนี้แก้ ssh user เป็น circleci หมดแล้ว แก้ terraform ใหม่แล้วด้วย`

- เพิ่ม step ที่ set fingerprint ให้กับ circle CI ด้วย วิธีอยู่ที่ [https://circleci.com/docs/2.0/add-ssh-key/](https://circleci.com/docs/2.0/add-ssh-key/)

## Q&A

- Canary Deploy (Advanced)
    - Spin Infra/server มาใหม่อีกชุด แล้วค่อยๆ drain traffic มาเครื่องใหม่ แล้ว down Infra/Server เก่าทิ้ง `Terraform ทำแบบนี้` เพราะอยากให้ Infra มัน Immutable
    - ต้องไปศึกษาว่าถ้าย้ายไป server ตัวใหม่แบบ automate ขนาดนี้จะย้ายพวก data, code ยังไง
- Ansible's Inventory เก็บแยกไฟล์ระหว่าง environment ดีกว่า เวลาใช้ก็ ansible -i <inventory>
