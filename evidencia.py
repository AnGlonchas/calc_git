─anglonchas at AnGlonchas in ~
╰─○ cd Programming/Python 
╭─anglonchas at AnGlonchas in ~/Programming/Python
╰─○ ls
Algorithms  CredentialReader  DataMining  Sqlmap  tmp  TRoD  VASMCompiler
╭─anglonchas at AnGlonchas in ~/Programming/Python
╰─○ mkdir calc
╭─anglonchas at AnGlonchas in ~/Programming/Python
╰─○ cd calc
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc
╰─○ ls
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc
╰─○ git init -b main 
Initialized empty Git repository in /home/anglonchas/Programming/Python/calc/.git/
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± touch main.py
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± st main.py
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	main.py

nothing added to commit but untracked files present (use "git add" to track)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git add main.py 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   main.py

╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git commit -m "Agregar suma"
[main (root-commit) 8cfed7f] Agregar suma
 1 file changed, 2 insertions(+)
 create mode 100644 main.py
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git diff
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git diff --staged
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git commit -m "Agregar resta"
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git add main.py 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git commit -m "Agregar resta"
[main 76abce2] Agregar resta
 1 file changed, 4 insertions(+), 1 deletion(-)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git add .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   main.py

╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git commit -m "Agregar multiplicar"
[main c376424] Agregar multiplicar
 1 file changed, 4 insertions(+), 1 deletion(-)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git add . 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   main.py

╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git commit -m "Agregar division"
[main 06e6fc6] Agregar division
 1 file changed, 6 insertions(+), 1 deletion(-)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git log --onelog
fatal: unrecognized argument: --onelog
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git log --oneline
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git status
On branch main
nothing to commit, working tree clean
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git diff
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git restore main.py 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git status
On branch main
nothing to commit, working tree clean
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± mkdir logs
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± echo "ejecucion correcta" > logs/app.log
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± echo "ejecucion correcta" > prueba.tmp  
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	logs/
	prueba.tmp

nothing added to commit but untracked files present (use "git add" to track)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± touch .gitignore
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± st .gitignore
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status      
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore

nothing added to commit but untracked files present (use "git add" to track)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status --ignored
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore

Ignored files:
  (use "git add -f <file>..." to include in what will be committed)
	logs/
	prueba.tmp

nothing added to commit but untracked files present (use "git add" to track)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± echo "Nueva ejecucion" >> logs/app.log          
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± cat logs/app.log
ejecucion correcta
Nueva ejecucion
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore

nothing added to commit but untracked files present (use "git add" to track)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± echo "Configuracion inicial" > config.txt
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git add config.txt
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git commit -m "Agregar configuracion"
[main ac4d424] Agregar configuracion
 1 file changed, 1 insertion(+)
 create mode 100644 config.txt
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± echo "Configuracion modificada" >> config.txt
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   config.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore

no changes added to commit (use "git add" and/or "git commit -a")
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git rm --cached config.txt
rm 'config.txt'
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git add .gitignore
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± git commit -m "Ignorar archivos locales" 
[main a8ed667] Ignorar archivos locales
 2 files changed, 16 insertions(+), 1 deletion(-)
 create mode 100644 .gitignore
 delete mode 100644 config.txt
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± echo "Otro cambio local" >> config.txt
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git status
On branch main
nothing to commit, working tree clean
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git check-ignore -v logs/app.log
.gitignore:2:*.log	logs/app.log
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git check-ignore -v prueba.tmp
.gitignore:5:*.tmp	prueba.tmp
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git check-ignore -v config.txt
.gitignore:16:config.txt	config.txt
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git status
On branch main
nothing to commit, working tree clean
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git log --oneline
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git switch -c trigonometria
Switched to a new branch 'trigonometria'
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✔
╰─± git branch
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✔
╰─± git add main.py 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✘✘✘
╰─± git commit -m "Agregar seno"
[trigonometria 7195fbe] Agregar seno
 1 file changed, 6 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✔
╰─± git add .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✘✘✘
╰─± git commit -m "Agregar coseno"
[trigonometria a5ba267] Agregar coseno
 1 file changed, 2 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✔
╰─± git add .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✘✘✘
╰─± git commit -m "Agregar tangente"
[trigonometria 3f39975] Agregar tangente
 1 file changed, 3 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✔
╰─± git log --oneline --graph --all --decorate  # Muestra ramas y commits.
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on trigonometria✔
╰─± git switch main                       # Activa la rama principal.
git merge --ff-only trigonometria     # Realiza un fast-forward.
Switched to branch 'main'
Updating a8ed667..3f39975
Fast-forward
 main.py | 11 +++++++++++
 1 file changed, 11 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git log --oneline --graph --all --decorate
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git reset --hard HEAD~3       # Retrocede main tres commits.
HEAD is now at a8ed667 Ignorar archivos locales
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git log --oneline --graph --all --decorate
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git merge --no-ff trigonometria -m "Fusionar trigonometria"
Merge made by the 'ort' strategy.
 main.py | 11 +++++++++++
 1 file changed, 11 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git switch -c exponenciales        # Crea y activa la rama.
Switched to a new branch 'exponenciales'
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on exponenciales✔
╰─± git add .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on exponenciales✘✘✘
╰─± git commit -m "agregar exponencial"
[exponenciales 0f717f9] agregar exponencial
 1 file changed, 3 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on exponenciales✔
╰─± git add .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on exponenciales✘✘✘
╰─± git status                                                        
On branch exponenciales
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   main.py

╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on exponenciales✘✘✘
╰─± git commit -m "agregar logaritmo"
[exponenciales 61cc879] agregar logaritmo
 1 file changed, 5 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on exponenciales✔
╰─± git switch main                   # Activa la rama principal.
git merge --no-ff exponenciales -m "Fusionar exponenciales"
git log --oneline --graph --all --decorate
Switched to branch 'main'
Merge made by the 'ort' strategy.
 main.py | 8 ++++++++
 1 file changed, 8 insertions(+)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git remote add origin https://github.com/anglonchas/calculadora_git_dvc.git  # Agrega remoto.
git remote -v                         # Comprueba la dirección remota.
git push -u origin main               # Publica la rama principal.
git push origin trigonometria         # Publica la rama trigonométrica.
git push origin exponenciales         # Publica la rama exponencial.
origin	https://github.com/anglonchas/calculadora_git_dvc.git (fetch)
origin	https://github.com/anglonchas/calculadora_git_dvc.git (push)
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git remote add origin https://github.com/AnGlonchas/calculadora_git_dvc.git  # Agrega remoto.
git remote -v                         # Comprueba la dirección remota.
git push -u origin main               # Publica la rama principal.
git push origin trigonometria         # Publica la rama trigonométrica.
git push origin exponenciales         # Publica la rama exponencial.
error: remote origin already exists.
origin	https://github.com/anglonchas/calculadora_git_dvc.git (fetch)
origin	https://github.com/anglonchas/calculadora_git_dvc.git (push)
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git remote add origin https://github.com/AnGlonchas/calc_git.git  # Agrega remoto.
git remote -v                         # Comprueba la dirección remota.
git push -u origin main               # Publica la rama principal.
git push origin trigonometria         # Publica la rama trigonométrica.
git push origin exponenciales         # Publica la rama exponencial.
error: remote origin already exists.
origin	https://github.com/anglonchas/calculadora_git_dvc.git (fetch)
origin	https://github.com/anglonchas/calculadora_git_dvc.git (push)
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± git remote add origin https://github.com/AnGlonchas/calc_git.git  # Agrega remoto.
git remote -v                         # Comprueba la dirección remota.
git push -u origin main               # Publica la rama principal.
git push origin trigonometria         # Publica la rama trigonométrica.
git push origin exponenciales         # Publica la rama exponencial.
error: remote origin already exists.
origin	https://github.com/anglonchas/calculadora_git_dvc.git (fetch)
origin	https://github.com/anglonchas/calculadora_git_dvc.git (push)
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± python -m pip install dvc      # Instala DVC.
dvc --version                 # Comprueba la instalación.
dvc init                      # Inicializa DVC en el repositorio.
zsh: command not found: python
zsh: command not found: dvc
zsh: command not found: dvc
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± python3 -m pip install dvc      # Instala DVC.
dvc --version                 # Comprueba la instalación.
dvc init                      # Inicializa DVC en el repositorio.
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.13/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
zsh: command not found: dvc
zsh: command not found: dvc
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± apt istall python3-dvc                        
Error: Invalid operation istall
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± apt install python3-dvc
Error: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
Error: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± sudo apt install python3-dvc
[sudo] password for anglonchas: 
Error: Unable to locate package python3-dvc
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔
╰─± python3 -m venv .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘
╰─± source ./bin/activate 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± python -m pip install dvc      # Instala DVC.
dvc --version                 # Comprueba la instalación.
dvc init                      # Inicializa DVC en el repositorio.
Collecting dvc
  Downloading dvc-3.67.1-py3-none-any.whl.metadata (17 kB)
Collecting attrs>=22.2.0 (from dvc)
  Using cached attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting celery (from dvc)
  Downloading celery-5.7.0-py3-none-any.whl.metadata (23 kB)
Collecting colorama>=0.3.9 (from dvc)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting configobj>=5.0.9 (from dvc)
  Downloading configobj-5.0.9-py2.py3-none-any.whl.metadata (3.2 kB)
Collecting distro>=1.3 (from dvc)
  Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting dpath<3,>=2.1.0 (from dvc)
  Downloading dpath-2.2.0-py3-none-any.whl.metadata (15 kB)
Collecting dulwich (from dvc)
  Downloading dulwich-1.2.21-cp313-cp313-manylinux_2_28_x86_64.whl.metadata (6.2 kB)
Collecting dvc-data<3.19.0,>=3.18.2 (from dvc)
  Downloading dvc_data-3.18.3-py3-none-any.whl.metadata (4.9 kB)
Collecting dvc-http>=2.29.0 (from dvc)
  Downloading dvc_http-2.32.0-py3-none-any.whl.metadata (1.3 kB)
Collecting dvc-objects (from dvc)
  Downloading dvc_objects-5.2.0-py3-none-any.whl.metadata (3.9 kB)
Collecting dvc-render<2,>=1.0.1 (from dvc)
  Downloading dvc_render-1.0.2-py3-none-any.whl.metadata (5.4 kB)
Collecting dvc-studio-client<1,>=0.21 (from dvc)
  Downloading dvc_studio_client-0.23.0-py3-none-any.whl.metadata (4.4 kB)
Collecting dvc-task<1,>=0.3.0 (from dvc)
  Downloading dvc_task-0.40.2-py3-none-any.whl.metadata (10.0 kB)
Collecting flatten-dict<1,>=0.4.1 (from dvc)
  Downloading flatten_dict-0.5.0-py3-none-any.whl.metadata (8.9 kB)
Collecting flufl.lock<10,>=8.1.0 (from dvc)
  Downloading flufl_lock-9.2.0-py3-none-any.whl.metadata (3.3 kB)
Collecting fsspec>=2024.2.0 (from dvc)
  Downloading fsspec-2026.9.0-py3-none-any.whl.metadata (10 kB)
Collecting funcy>=1.14 (from dvc)
  Downloading funcy-2.1-py3-none-any.whl.metadata (6.3 kB)
Collecting grandalf<1,>=0.7 (from dvc)
  Downloading grandalf-0.8-py3-none-any.whl.metadata (1.7 kB)
Collecting gto<2,>=1.6.0 (from dvc)
  Downloading gto-1.10.1-py3-none-any.whl.metadata (4.8 kB)
Collecting hydra-core>=1.1 (from dvc)
  Downloading hydra_core-1.3.8-py3-none-any.whl.metadata (5.7 kB)
Collecting iterative-telemetry>=0.0.7 (from dvc)
  Downloading iterative_telemetry-0.0.10-py3-none-any.whl.metadata (4.1 kB)
Collecting kombu (from dvc)
  Downloading kombu-5.7.0-py3-none-any.whl.metadata (17 kB)
Collecting networkx>=2.5 (from dvc)
  Using cached networkx-3.7-py3-none-any.whl.metadata (6.7 kB)
Collecting omegaconf (from dvc)
  Downloading omegaconf-2.4.0-py3-none-any.whl.metadata (4.9 kB)
Collecting packaging>=19 (from dvc)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pathspec<2,>=0.10.3 (from dvc)
  Using cached pathspec-1.1.1-py3-none-any.whl.metadata (14 kB)
Collecting platformdirs<5,>=3.1.1 (from dvc)
  Downloading platformdirs-4.14.5-py3-none-any.whl.metadata (5.7 kB)
Collecting psutil>=5.8 (from dvc)
  Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl.metadata (22 kB)
Collecting pydot>=1.2.4 (from dvc)
  Downloading pydot-4.0.1-py3-none-any.whl.metadata (11 kB)
Collecting pygtrie>=2.3.2 (from dvc)
  Downloading pygtrie-2.6.2-py3-none-any.whl.metadata (12 kB)
Collecting pyparsing>=3.0.0 (from dvc)
  Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)
Collecting requests>=2.22 (from dvc)
  Using cached requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting rich>=12 (from dvc)
  Using cached rich-15.0.0-py3-none-any.whl.metadata (18 kB)
Collecting ruamel.yaml>=0.17.11 (from dvc)
  Downloading ruamel_yaml-0.19.1-py3-none-any.whl.metadata (16 kB)
Collecting scmrepo<4,>=3.5.2 (from dvc)
  Downloading scmrepo-3.6.2-py3-none-any.whl.metadata (4.8 kB)
Collecting shortuuid>=0.5 (from dvc)
  Downloading shortuuid-1.0.13-py3-none-any.whl.metadata (5.8 kB)
Collecting shtab<2,>=1.3.4 (from dvc)
  Downloading shtab-1.13.0-py3-none-any.whl.metadata (7.6 kB)
Collecting tabulate>=0.8.7 (from dvc)
  Using cached tabulate-0.10.0-py3-none-any.whl.metadata (40 kB)
Collecting tomlkit>=0.11.1 (from dvc)
  Downloading tomlkit-0.15.2-py3-none-any.whl.metadata (3.4 kB)
Collecting tqdm<5,>=4.63.1 (from dvc)
  Downloading tqdm-4.70.1-py3-none-any.whl.metadata (57 kB)
Collecting voluptuous>=0.11.7 (from dvc)
  Downloading voluptuous-0.16.0-py3-none-any.whl.metadata (20 kB)
Collecting zc.lockfile>=1.2.1 (from dvc)
  Downloading zc_lockfile-4.1-py3-none-any.whl.metadata (6.8 kB)
Collecting dictdiffer>=0.8.1 (from dvc-data<3.19.0,>=3.18.2->dvc)
  Downloading dictdiffer-0.10.0-py3-none-any.whl.metadata (2.9 kB)
Collecting diskcache>=5.2.1 (from dvc-data<3.19.0,>=3.18.2->dvc)
  Downloading diskcache-5.6.3-py3-none-any.whl.metadata (20 kB)
Collecting sqltrie<1,>=0.11.0 (from dvc-data<3.19.0,>=3.18.2->dvc)
  Downloading sqltrie-0.11.3-py3-none-any.whl.metadata (3.5 kB)
Collecting orjson<4,>=3 (from dvc-data<3.19.0,>=3.18.2->dvc)
  Downloading orjson-3.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (42 kB)
Collecting billiard>=4.3.2 (from celery->dvc)
  Downloading billiard-4.3.2-py3-none-any.whl.metadata (5.0 kB)
Collecting vine<6.0,>=5.1.0 (from celery->dvc)
  Downloading vine-5.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting click<9.0,>=8.3.1 (from celery->dvc)
  Using cached click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting click-didyoumean>=0.3.1 (from celery->dvc)
  Downloading click_didyoumean-0.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting click-repl>=0.4.1 (from celery->dvc)
  Downloading click_repl-0.4.1-py3-none-any.whl.metadata (3.7 kB)
Collecting click-plugins>=1.1.1.2 (from celery->dvc)
  Downloading click_plugins-1.1.1.2-py2.py3-none-any.whl.metadata (6.5 kB)
Collecting python-dateutil==2.9.0.post0 (from celery->dvc)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting tzlocal (from celery->dvc)
  Downloading tzlocal-5.4.5-py3-none-any.whl.metadata (7.7 kB)
Collecting six>=1.5 (from python-dateutil==2.9.0.post0->celery->dvc)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting atpublic (from flufl.lock<10,>=8.1.0->dvc)
  Downloading atpublic-9.0.0-py3-none-any.whl.metadata (2.6 kB)
Collecting entrypoints (from gto<2,>=1.6.0->dvc)
  Downloading entrypoints-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting pydantic>=2 (from gto<2,>=1.6.0->dvc)
  Downloading pydantic-2.14.3-py3-none-any.whl.metadata (141 kB)
Collecting pydantic-settings>=2 (from gto<2,>=1.6.0->dvc)
  Downloading pydantic_settings-2.16.2-py3-none-any.whl.metadata (4.0 kB)
Collecting semver>=2.13.0 (from gto<2,>=1.6.0->dvc)
  Downloading semver-3.1.0-py3-none-any.whl.metadata (6.9 kB)
Collecting amqp>=5.4.2 (from kombu->dvc)
  Downloading amqp-5.4.2-py3-none-any.whl.metadata (9.4 kB)
Collecting gitpython>3 (from scmrepo<4,>=3.5.2->dvc)
  Downloading gitpython-3.2.1-py3-none-any.whl.metadata (13 kB)
Collecting pygit2>=1.14.0 (from scmrepo<4,>=3.5.2->dvc)
  Downloading pygit2-1.21.0-cp313-cp313-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.7 kB)
Collecting asyncssh<3,>=2.13.1 (from scmrepo<4,>=3.5.2->dvc)
  Downloading asyncssh-2.24.1-py3-none-any.whl.metadata (9.8 kB)
Collecting aiohttp-retry>=2.5.0 (from scmrepo<4,>=3.5.2->dvc)
  Downloading aiohttp_retry-2.9.1-py3-none-any.whl.metadata (8.8 kB)
Collecting cryptography>=48.0.1 (from asyncssh<3,>=2.13.1->scmrepo<4,>=3.5.2->dvc)
  Using cached cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.4 kB)
Collecting typing_extensions>=4.0.0 (from asyncssh<3,>=2.13.1->scmrepo<4,>=3.5.2->dvc)
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting urllib3>=2.2.2 (from dulwich->dvc)
  Using cached urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting aiohttp (from aiohttp-retry>=2.5.0->scmrepo<4,>=3.5.2->dvc)
  Using cached aiohttp-3.14.5-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.3 kB)
Collecting prompt_toolkit>=3.0.36 (from click-repl>=0.4.1->celery->dvc)
  Using cached prompt_toolkit-3.0.53-py3-none-any.whl.metadata (6.4 kB)
Collecting cffi>=2.0.0 (from cryptography>=48.0.1->asyncssh<3,>=2.13.1->scmrepo<4,>=3.5.2->dvc)
  Using cached cffi-2.1.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.5 kB)
Collecting pycparser (from cffi>=2.0.0->cryptography>=48.0.1->asyncssh<3,>=2.13.1->scmrepo<4,>=3.5.2->dvc)
  Using cached pycparser-3.12-py3-none-any.whl.metadata (9.7 kB)
Collecting gitdb<5,>=4.0.1 (from gitpython>3->scmrepo<4,>=3.5.2->dvc)
  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython>3->scmrepo<4,>=3.5.2->dvc)
  Downloading smmap-5.0.3-py3-none-any.whl.metadata (4.6 kB)
Collecting omegaconf (from dvc)
  Downloading omegaconf-2.3.1-py3-none-any.whl.metadata (4.5 kB)
Collecting antlr4-python3-runtime==4.9.* (from hydra-core>=1.1->dvc)
  Downloading antlr4-python3-runtime-4.9.3.tar.gz (117 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting PyYAML>=5.1.0 (from omegaconf->dvc)
  Using cached pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting appdirs (from iterative-telemetry>=0.0.7->dvc)
  Downloading appdirs-1.4.4-py2.py3-none-any.whl.metadata (9.0 kB)
Collecting filelock (from iterative-telemetry>=0.0.7->dvc)
  Downloading filelock-4.2.9-py3-none-any.whl.metadata (2.3 kB)
Collecting wcwidth>=0.1.4 (from prompt_toolkit>=3.0.36->click-repl>=0.4.1->celery->dvc)
  Using cached wcwidth-0.9.4-cp310-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (23 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2->gto<2,>=1.6.0->dvc)
  Downloading annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.50.4 (from pydantic>=2->gto<2,>=1.6.0->dvc)
  Downloading pydantic_core-2.50.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (6.6 kB)
Collecting typing-inspection>=0.4.4 (from pydantic>=2->gto<2,>=1.6.0->dvc)
  Downloading typing_inspection-0.4.5-py3-none-any.whl.metadata (2.6 kB)
Collecting python-dotenv>=1.2.2 (from pydantic-settings>=2->gto<2,>=1.6.0->dvc)
  Downloading python_dotenv-1.2.4-py3-none-any.whl.metadata (29 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.22->dvc)
  Using cached charset_normalizer-3.5.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (46 kB)
Collecting idna<4,>=2.5 (from requests>=2.22->dvc)
  Using cached idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting certifi>=2023.5.7 (from requests>=2.22->dvc)
  Using cached certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=12->dvc)
  Using cached markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich>=12->dvc)
  Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=12->dvc)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp->aiohttp-retry>=2.5.0->scmrepo<4,>=3.5.2->dvc)
  Using cached aiohappyeyeballs-2.7.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp->aiohttp-retry>=2.5.0->scmrepo<4,>=3.5.2->dvc)
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting frozenlist>=1.1.1 (from aiohttp->aiohttp-retry>=2.5.0->scmrepo<4,>=3.5.2->dvc)
  Using cached frozenlist-1.8.0-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<8.0,>=4.5 (from aiohttp->aiohttp-retry>=2.5.0->scmrepo<4,>=3.5.2->dvc)
  Using cached multidict-7.2.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (6.1 kB)
Collecting propcache>=0.2.0 (from aiohttp->aiohttp-retry>=2.5.0->scmrepo<4,>=3.5.2->dvc)
  Using cached propcache-0.5.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (25 kB)
Collecting yarl<2.0,>=1.25.1 (from aiohttp->aiohttp-retry>=2.5.0->scmrepo<4,>=3.5.2->dvc)
  Using cached yarl-1.25.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (111 kB)
Downloading dvc-3.67.1-py3-none-any.whl (470 kB)
Downloading dpath-2.2.0-py3-none-any.whl (17 kB)
Downloading dvc_data-3.18.3-py3-none-any.whl (79 kB)
Downloading dvc_objects-5.2.0-py3-none-any.whl (33 kB)
Downloading dvc_render-1.0.2-py3-none-any.whl (22 kB)
Downloading dvc_studio_client-0.23.0-py3-none-any.whl (16 kB)
Downloading dvc_task-0.40.2-py3-none-any.whl (21 kB)
Downloading celery-5.7.0-py3-none-any.whl (519 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached click-8.5.0-py3-none-any.whl (125 kB)
Downloading flatten_dict-0.5.0-py3-none-any.whl (9.9 kB)
Downloading flufl_lock-9.2.0-py3-none-any.whl (11 kB)
Downloading grandalf-0.8-py3-none-any.whl (41 kB)
Downloading gto-1.10.1-py3-none-any.whl (45 kB)
Downloading kombu-5.7.0-py3-none-any.whl (266 kB)
Downloading vine-5.1.0-py3-none-any.whl (9.6 kB)
Downloading orjson-3.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (130 kB)
Using cached pathspec-1.1.1-py3-none-any.whl (57 kB)
Downloading platformdirs-4.14.5-py3-none-any.whl (35 kB)
Downloading scmrepo-3.6.2-py3-none-any.whl (74 kB)
Downloading asyncssh-2.24.1-py3-none-any.whl (382 kB)
Downloading dulwich-1.2.21-cp313-cp313-manylinux_2_28_x86_64.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 1.0 MB/s eta 0:00:00
Downloading shtab-1.13.0-py3-none-any.whl (22 kB)
Downloading sqltrie-0.11.3-py3-none-any.whl (17 kB)
Downloading tqdm-4.70.1-py3-none-any.whl (80 kB)
Downloading aiohttp_retry-2.9.1-py3-none-any.whl (10.0 kB)
Downloading amqp-5.4.2-py3-none-any.whl (51 kB)
Using cached attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading billiard-4.3.2-py3-none-any.whl (90 kB)
Downloading click_didyoumean-0.3.1-py3-none-any.whl (3.6 kB)
Downloading click_plugins-1.1.1.2-py2.py3-none-any.whl (11 kB)
Downloading click_repl-0.4.1-py3-none-any.whl (14 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading configobj-5.0.9-py2.py3-none-any.whl (35 kB)
Using cached cryptography-50.0.2-cp311-abi3-manylinux_2_34_x86_64.whl (4.8 MB)
Using cached cffi-2.1.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (221 kB)
Downloading dictdiffer-0.10.0-py3-none-any.whl (16 kB)
Downloading diskcache-5.6.3-py3-none-any.whl (45 kB)
Downloading distro-1.9.0-py3-none-any.whl (20 kB)
Downloading dvc_http-2.32.0-py3-none-any.whl (12 kB)
Downloading fsspec-2026.9.0-py3-none-any.whl (221 kB)
Downloading funcy-2.1-py3-none-any.whl (29 kB)
Downloading gitpython-3.2.1-py3-none-any.whl (231 kB)
Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
Downloading smmap-5.0.3-py3-none-any.whl (24 kB)
Downloading hydra_core-1.3.8-py3-none-any.whl (168 kB)
Downloading omegaconf-2.3.1-py3-none-any.whl (79 kB)
Downloading iterative_telemetry-0.0.10-py3-none-any.whl (10 kB)
Using cached networkx-3.7-py3-none-any.whl (2.1 MB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached prompt_toolkit-3.0.53-py3-none-any.whl (392 kB)
Downloading psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl (155 kB)
Downloading pydantic-2.14.3-py3-none-any.whl (494 kB)
Downloading pydantic_core-2.50.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 1.2 MB/s eta 0:00:00
Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB)
Downloading pydantic_settings-2.16.2-py3-none-any.whl (81 kB)
Downloading pydot-4.0.1-py3-none-any.whl (37 kB)
Downloading pygit2-1.21.0-cp313-cp313-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (4.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 1.8 MB/s eta 0:00:00
Downloading pygtrie-2.6.2-py3-none-any.whl (33 kB)
Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)
Downloading python_dotenv-1.2.4-py3-none-any.whl (23 kB)
Using cached pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (801 kB)
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Using cached charset_normalizer-3.5.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (254 kB)
Using cached idna-3.20-py3-none-any.whl (69 kB)
Using cached urllib3-2.8.0-py3-none-any.whl (135 kB)
Using cached certifi-2026.10.23-py3-none-any.whl (135 kB)
Using cached rich-15.0.0-py3-none-any.whl (310 kB)
Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
Using cached markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading ruamel_yaml-0.19.1-py3-none-any.whl (118 kB)
Downloading semver-3.1.0-py3-none-any.whl (18 kB)
Downloading shortuuid-1.0.13-py3-none-any.whl (10 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tabulate-0.10.0-py3-none-any.whl (39 kB)
Downloading tomlkit-0.15.2-py3-none-any.whl (52 kB)
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Downloading typing_inspection-0.4.5-py3-none-any.whl (14 kB)
Downloading voluptuous-0.16.0-py3-none-any.whl (31 kB)
Using cached wcwidth-0.9.4-cp310-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (785 kB)
Downloading zc_lockfile-4.1-py3-none-any.whl (9.2 kB)
Using cached aiohttp-3.14.5-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.9 MB)
Using cached multidict-7.2.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (516 kB)
Using cached yarl-1.25.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (117 kB)
Using cached aiohappyeyeballs-2.7.1-py3-none-any.whl (15 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached frozenlist-1.8.0-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (234 kB)
Using cached propcache-0.5.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (234 kB)
Downloading appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
Downloading atpublic-9.0.0-py3-none-any.whl (11 kB)
Downloading entrypoints-0.4.2-py3-none-any.whl (5.3 kB)
Downloading filelock-4.2.9-py3-none-any.whl (164 kB)
Using cached pycparser-3.12-py3-none-any.whl (62 kB)
Downloading tzlocal-5.4.5-py3-none-any.whl (18 kB)
Building wheels for collected packages: antlr4-python3-runtime
  Building wheel for antlr4-python3-runtime (pyproject.toml) ... done
  Created wheel for antlr4-python3-runtime: filename=antlr4_python3_runtime-4.9.3-py3-none-any.whl size=144590 sha256=cf5f225060aca3d063647f407de6febc403f8441095debfd4255f591942d3606
  Stored in directory: /home/anglonchas/.cache/pip/wheels/d5/b3/74/a35b66048c9de6631cd74cbc9475e6feb3e69a467983446bd8
Successfully built antlr4-python3-runtime
Installing collected packages: funcy, appdirs, antlr4-python3-runtime, zc.lockfile, wcwidth, voluptuous, vine, urllib3, tzlocal, typing_extensions, tqdm, tomlkit, tabulate, smmap, six, shtab, shortuuid, semver, ruamel.yaml, PyYAML, python-dotenv, pyparsing, pygtrie, pygments, pycparser, psutil, propcache, platformdirs, pathspec, packaging, orjson, networkx, multidict, mdurl, idna, fsspec, frozenlist, flatten-dict, filelock, entrypoints, dvc-render, dpath, distro, diskcache, dictdiffer, configobj, colorama, click, charset_normalizer, certifi, billiard, attrs, atpublic, annotated-types, aiohappyeyeballs, yarl, typing-inspection, sqltrie, requests, python-dateutil, pydot, pydantic-core, prompt_toolkit, omegaconf, markdown-it-py, grandalf, gitdb, flufl.lock, dvc-objects, dulwich, click-plugins, click-didyoumean, cffi, amqp, aiosignal, rich, pygit2, pydantic, kombu, iterative-telemetry, hydra-core, gitpython, dvc-studio-client, dvc-data, cryptography, click-repl, aiohttp, pydantic-settings, celery, asyncssh, aiohttp-retry, scmrepo, dvc-task, dvc-http, gto, dvc
Successfully installed PyYAML-6.0.3 aiohappyeyeballs-2.7.1 aiohttp-3.14.5 aiohttp-retry-2.9.1 aiosignal-1.4.0 amqp-5.4.2 annotated-types-0.8.0 antlr4-python3-runtime-4.9.3 appdirs-1.4.4 asyncssh-2.24.1 atpublic-9.0.0 attrs-26.1.0 billiard-4.3.2 celery-5.7.0 certifi-2026.10.23 cffi-2.1.1 charset_normalizer-3.5.2 click-8.5.0 click-didyoumean-0.3.1 click-plugins-1.1.1.2 click-repl-0.4.1 colorama-0.4.6 configobj-5.0.9 cryptography-50.0.2 dictdiffer-0.10.0 diskcache-5.6.3 distro-1.9.0 dpath-2.2.0 dulwich-1.2.21 dvc-3.67.1 dvc-data-3.18.3 dvc-http-2.32.0 dvc-objects-5.2.0 dvc-render-1.0.2 dvc-studio-client-0.23.0 dvc-task-0.40.2 entrypoints-0.4.2 filelock-4.2.9 flatten-dict-0.5.0 flufl.lock-9.2.0 frozenlist-1.8.0 fsspec-2026.9.0 funcy-2.1 gitdb-4.0.12 gitpython-3.2.1 grandalf-0.8 gto-1.10.1 hydra-core-1.3.8 idna-3.20 iterative-telemetry-0.0.10 kombu-5.7.0 markdown-it-py-4.2.0 mdurl-0.1.2 multidict-7.2.1 networkx-3.7 omegaconf-2.3.1 orjson-3.13.0 packaging-26.3 pathspec-1.1.1 platformdirs-4.14.5 prompt_toolkit-3.0.53 propcache-0.5.4 psutil-7.2.2 pycparser-3.12 pydantic-2.14.3 pydantic-core-2.50.4 pydantic-settings-2.16.2 pydot-4.0.1 pygit2-1.21.0 pygments-2.21.0 pygtrie-2.6.2 pyparsing-3.3.3 python-dateutil-2.9.0.post0 python-dotenv-1.2.4 requests-2.34.2 rich-15.0.0 ruamel.yaml-0.19.1 scmrepo-3.6.2 semver-3.1.0 shortuuid-1.0.13 shtab-1.13.0 six-1.17.0 smmap-5.0.3 sqltrie-0.11.3 tabulate-0.10.0 tomlkit-0.15.2 tqdm-4.70.1 typing-inspection-0.4.5 typing_extensions-4.16.0 tzlocal-5.4.5 urllib3-2.8.0 vine-5.1.0 voluptuous-0.16.0 wcwidth-0.9.4 yarl-1.25.1 zc.lockfile-4.1
3.67.1
ERROR: failed to initiate DVC - /home/anglonchas/Programming/Python/calc/.dvc is ignored by your SCM tool. 
Make sure that it's tracked, for example, by adding '!.dvc' to .gitignore.
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git statuss
git: 'statuss' is not a git command. See 'git --help'.

The most similar command is
	status
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git status 
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± dvc init
ERROR: failed to initiate DVC - /home/anglonchas/Programming/Python/calc/.dvc is ignored by your SCM tool. 
Make sure that it's tracked, for example, by adding '!.dvc' to .gitignore.
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± st .git
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± st .gitignore 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± dvc init     
Initialized DVC repository.

You can now commit the changes to git.

+---------------------------------------------------------------------+
|                                                                     |
|        DVC has enabled anonymous aggregate usage analytics.         |
|     Read the analytics documentation (and how to opt-out) here:     |
|             <https://dvc.org/doc/user-guide/analytics>              |
|                                                                     |
+---------------------------------------------------------------------+

What's next?
------------
- Check out the documentation: <https://dvc.org/doc>
- Get help and share ideas: <https://dvc.org/chat>
- Star us on GitHub: <https://github.com/treeverse/dvc>
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git status                    # Observa los archivos creados.
git add .dvc                  # Prepara la configuración.
git commit -m "Inicializar DVC"
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git add .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git commit -m "dvc" 
[main 982dc67] dvc
 1 file changed, 3 insertions(+), 16 deletions(-)
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± mkdir scripts                  # Crea la carpeta de scripts.
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± touch scripts/generar_datos.py
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± st scripts/generar_datos.py
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± python -m scripts.generar_datos --n 100 --seed 42
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/anglonchas/Programming/Python/calc/scripts/generar_datos.py", line 5, in <module>
    from calculadora import sumar, restar, multiplicar, dividir  # Importa funciones.
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'calculadora'
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± python -m scripts.generar_datos --n 100 --seed 42
Dataset generado: 100 registros
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± dvc add datos/operaciones.csv     # Comienza a versionar el dataset.
ERROR: bad DVC file name 'datos/operaciones.csv.dvc' is git-ignored.                            
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± ls
bin  config.txt  datos  include  lib  lib64  logs  main.py  prueba.tmp  __pycache__  pyvenv.cfg  scripts
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± cd datos
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc/datos on main✔ using «calc»
╰─± s
zsh: command not found: s
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc/datos on main✔ using «calc»
╰─± ls
operaciones.csv
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc/datos on main✔ using «calc»
╰─± cd .
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc/datos on main✔ using «calc»
╰─± cd ..
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± git add . 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± git status
On branch main
nothing to commit, working tree clean
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± dvc add datos/operaciones.csv     # Comienza a versionar el dataset.
ERROR: bad DVC file name 'datos/operaciones.csv.dvc' is git-ignored.                            
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✔ using «calc»
╰─± dvc add datos/operaciones.csv     # Comienza a versionar el dataset.
100% Adding...|████████████████████████████████████████████████████████████████████████|1/1 [00:00, 14.88file/s]
                                                                                                                
To track the changes with git, run:

	git add datos/operaciones.csv.dvc datos/.gitignore .dvc/.gitignore

To enable auto staging, run:

	dvc config core.autostage true
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git add scripts/generar_datos.py      # Versiona el generador.
git add datos/operaciones.csv.dvc     # Versiona la referencia DVC.
git add datos/.gitignore              # Versiona las exclusiones.
git commit -m "Dataset V1 - 100 registros"
[main 0314e74] Dataset V1 - 100 registros
 3 files changed, 39 insertions(+)
 create mode 100644 datos/.gitignore
 create mode 100644 datos/operaciones.csv.dvc
 create mode 100644 scripts/generar_datos.py
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git status                            # Comprueba los cambios pendientes.
dvc status                            # Comprueba el estado de DVC.
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   .gitignore

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.dvc/
	.dvcignore
	__pycache__/
	bin/
	config.txt
	lib/
	lib64
	logs/
	prueba.tmp
	pyvenv.cfg
	scripts/__pycache__/

no changes added to commit (use "git add" and/or "git commit -a")
Data and pipelines are up to date.                                                                              
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± mkdir -p ../almacen_dvc                # Crea una carpeta externa.
dvc remote add -d almacen ../almacen_dvc  # Configura el remoto.
git add .dvc/config                    # Prepara la configuración.
git commit -m "Configurar remoto DVC"  # Registra el remoto.
dvc push                               # Envía V1 al almacenamiento.
Setting 'almacen' as a default remote.
[main d38ecab] Configurar remoto DVC
 1 file changed, 4 insertions(+)
 create mode 100644 .dvc/config
Collecting                                                                            |1.00 [00:00, 69.3entry/s]
Pushing
1 file pushed                                                                                                   
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± python -m scripts.generar_datos --n 200 --seed 42  # Genera V2.
dvc status                                         # Detecta cambios.
dvc add datos/operaciones.csv                      # Actualiza el hash.
git add datos/operaciones.csv.dvc                   # Prepara referencia.
git commit -m "Dataset V2 - 200 registros"         # Registra V2.
dvc push                                           # Almacena V2.
Dataset generado: 200 registros
datos/operaciones.csv.dvc:                                                                                      
	changed outs:
		modified:           datos/operaciones.csv
100% Adding...|████████████████████████████████████████████████████████████████████████|1/1 [00:00, 20.62file/s]
                                                                                                                
To track the changes with git, run:

	git add datos/operaciones.csv.dvc

To enable auto staging, run:

	dvc config core.autostage true
[main 023348f] Dataset V2 - 200 registros
 1 file changed, 2 insertions(+), 2 deletions(-)
Collecting                                                                            |1.00 [00:00,  120entry/s]
Pushing
1 file pushed                                                                                                   
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± python -m scripts.generar_datos --n 300 --seed 42  # Genera V3.
dvc add datos/operaciones.csv                      # Registra contenido.
git add datos/operaciones.csv.dvc                   # Prepara referencia.
git commit -m "Dataset V3 - 300 registros"         # Registra V3.
dvc push                                           # Almacena V3.
Dataset generado: 300 registros
100% Adding...|████████████████████████████████████████████████████████████████████████|1/1 [00:00, 22.99file/s]
                                                                                                                
To track the changes with git, run:

	git add datos/operaciones.csv.dvc

To enable auto staging, run:

	dvc config core.autostage true
[main 67408d4] Dataset V3 - 300 registros
 1 file changed, 2 insertions(+), 2 deletions(-)
Collecting                                                                            |1.00 [00:00, 89.9entry/s]
Pushing
1 file pushed                                                                                                   
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± python -c "import csv; print(sum(1 for _ in csv.DictReader(open('datos/operaciones.csv'))))"
300
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git log --oneline --decorate
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git switch -c recuperar-v1 HASH_V1  # Sustituye HASH_V1 por el hash real.
dvc checkout                       # Recupera el contenido de V1.
fatal: invalid reference: HASH_V1
Building workspace index                                                              |2.00 [00:00, 81.6entry/s]
Comparing indexes                                                                     |3.00 [00:00,  709entry/s]
Applying changes                                                                      |0.00 [00:00,     ?file/s]
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± python -c "import csv; print(sum(1 for _ in csv.DictReader(open('datos/operaciones.csv'))))"
300
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git switch main                    # Regresa a la versión actual.
dvc checkout                       # Recupera el dataset V3.
M	.gitignore
Already on 'main'
Building workspace index                                                              |2.00 [00:00,  118entry/s]
Comparing indexes                                                                     |3.00 [00:00,  507entry/s]
Applying changes                                                                      |0.00 [00:00,     ?file/s]
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git push origin main               # Publica los commits de DVC.
remote: Repository not found.
fatal: repository 'https://github.com/anglonchas/calculadora_git_dvc.git/' not found
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git remote set-url origin https://github.com/AnGlonchas/calc                 
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git push origin main               # Publica los commits de DVC.
remote: Repository not found.
fatal: repository 'https://github.com/AnGlonchas/calc/' not found
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git remote set-url origin https://github.com/AnGlonchas/calc_git
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± cd ..                              # Regresa a la carpeta superior.
git clone https://github.com/USUARIO/calculadora_git_dvc.git copia_calculadora
cd copia_calculadora               # Entra al repositorio clonado.
Cloning into 'copia_calculadora'...
remote: Repository not found.
fatal: repository 'https://github.com/USUARIO/calculadora_git_dvc.git/' not found
cd: no such file or directory: copia_calculadora
╭─anglonchas at AnGlonchas in ~/Programming/Python using «calc»
╰─○ cd ..                              # Regresa a la carpeta superior.
git clone https://github.com/AnGlonchas/calc_git.git copia_calculadora
cd copia_calculadora               # Entra al repositorio clonado.
Cloning into 'copia_calculadora'...
warning: You appear to have cloned an empty repository.
╭─anglonchas at AnGlonchas in ~/Programming/copia_calculadora on main✔ using «calc»
╰─± dvc status                         # Comprueba el estado de los datos.
dvc pull                           # Descarga y materializa los datos.
ERROR: you are not inside of a DVC repository (checked up to mount point '/')
ERROR: you are not inside of a DVC repository (checked up to mount point '/')
╭─anglonchas at AnGlonchas in ~/Programming/copia_calculadora on main✔ using «calc»
╰─± python -c "import csv; print(sum(1 for _ in csv.DictReader(open('datos/operaciones.csv'))))"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import csv; print(sum(1 for _ in csv.DictReader(open('datos/operaciones.csv'))))
                                                    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'datos/operaciones.csv'
╭─anglonchas at AnGlonchas in ~/Programming/copia_calculadora on main✔ using «calc»
╰─± dvc stage add -n resumen \
  -d scripts/procesar.py \
  -d datos/operaciones.csv \
  -o resultados/resumen.csv \
  python -m scripts.procesar
ERROR: you are not inside of a DVC repository (checked up to mount point '/')
╭─anglonchas at AnGlonchas in ~/Programming/copia_calculadora on main✔ using «calc»
╰─± ls
╭─anglonchas at AnGlonchas in ~/Programming/copia_calculadora on main✔ using «calc»
╰─± cd ..
╭─anglonchas at AnGlonchas in ~/Programming using «calc»
╰─○ ls
 C                   Cpp             Dart  'Nim Manual_files'   Notes    Python   TS       Web
 copia_calculadora   Cybersecurity   Nim   'Nim Manual.html'    Prolog   tmp      VMware
╭─anglonchas at AnGlonchas in ~/Programming using «calc»
╰─○ cd Python            
╭─anglonchas at AnGlonchas in ~/Programming/Python using «calc»
╰─○ cd calc
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± dvc stage add -n resumen \
  -d scripts/procesar.py \
  -d datos/operaciones.csv \
  -o resultados/resumen.csv \
  python -m scripts.procesar
Could not create .gitignore entry in /home/anglonchas/Programming/Python/calc/resultados/.gitignore. DVC will attempt to create .gitignore entry again when the stage is run.
Added stage 'resumen' in 'dvc.yaml'

To track the changes with git, run:

	git add dvc.yaml

To enable auto staging, run:

	dvc config core.autostage true
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± stages:
  resumen:
    cmd: python -m scripts.procesar
    deps:
      - scripts/procesar.py
      - datos/operaciones.csv
    outs:
      - resultados/resumen.csv
zsh: command not found: stages:
zsh: command not found: resumen:
zsh: command not found: cmd:
zsh: command not found: deps:
cd: string not in pwd: -
cd: string not in pwd: -
zsh: command not found: outs:
cd: string not in pwd: -
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± st dvc.yaml               
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± dvc repro                         # Ejecuta las etapas necesarias.
'datos/operaciones.csv.dvc' didn't change, skipping                                                             
Running stage 'resumen':                                                                                        
> python -m scripts.procesar
Resumen generado correctamente
Generating lock file 'dvc.lock'                                                                                 
Updating lock file 'dvc.lock'

To track the changes with git, run:

	git add dvc.lock resultados/.gitignore

To enable auto staging, run:

	dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± python -m scripts.generar_datos --n 500 --seed 42  # Genera 500 registros.
dvc add datos/operaciones.csv                      # Versiona el contenido.
dvc status                                         # Detecta cambios.
dvc repro                                          # Actualiza el resumen.
Dataset generado: 500 registros
100% Adding...|████████████████████████████████████████████████████████████████████████|1/1 [00:00, 18.66file/s]
                                                                                                                
To track the changes with git, run:

	git add datos/operaciones.csv.dvc

To enable auto staging, run:

	dvc config core.autostage true
resumen:                                                                                                        
	changed deps:
		modified:           datos/operaciones.csv
'datos/operaciones.csv.dvc' didn't change, skipping                                                             
Running stage 'resumen':                                                                                        
> python -m scripts.procesar
Resumen generado correctamente
Updating lock file 'dvc.lock'                                                                                   

To track the changes with git, run:

	git add dvc.lock

To enable auto staging, run:

	dvc config core.autostage true
Use `dvc push` to send your updates to remote storage.
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± git add datos/operaciones.csv.dvc    # Registra versión del dataset.
git add scripts/procesar.py          # Registra script de procesamiento.
git add dvc.yaml dvc.lock            # Registra pipeline y estado.
git add resultados/.gitignore        # Registra exclusión de la salida.
git commit -m "Dataset V4 y pipeline de resumen"
dvc push                             # Almacena datos y resultados.
git push origin main                 # Publica código y metadatos.
[main f239955] Dataset V4 y pipeline de resumen
 5 files changed, 55 insertions(+), 2 deletions(-)
 create mode 100644 dvc.lock
 create mode 100644 dvc.yaml
 create mode 100644 resultados/.gitignore
 create mode 100644 scripts/procesar.py
Collecting                                                                            |2.00 [00:00,  162entry/s]
Pushing
2 files pushed                                                                                                  
Enumerating objects: 67, done.
Counting objects: 100% (67/67), done.
Delta compression using up to 4 threads
Compressing objects: 100% (57/57), done.
Writing objects: 100% (67/67), 8.14 KiB | 694.00 KiB/s, done.
Total 67 (delta 14), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (14/14), done.
To https://github.com/AnGlonchas/calc_git
 * [new branch]      main -> main
╭─anglonchas at AnGlonchas in ~/Programming/Python/calc on main✘✘✘ using «calc»
╰─± 

