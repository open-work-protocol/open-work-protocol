from pathlib import Path
import shutil, subprocess, tempfile

class WorkspaceError(RuntimeError): pass

def _git(cwd, *args):
    p=subprocess.run(['git',*args],cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if p.returncode:
        raise WorkspaceError(p.stderr.strip() or 'git command failed')
    return p.stdout.strip()

def provision_git_workspace(goal: str, parent: str | None = None):
    root=Path(tempfile.mkdtemp(prefix='owp-work-',dir=parent))
    _git(root,'init','-q')
    _git(root,'config','user.email','reference@openwork.invalid')
    _git(root,'config','user.name','OWP Reference Gateway')
    (root/'WORK_REQUEST.md').write_text('# Work request\n\n'+goal.strip()+'\n',encoding='utf-8')
    _git(root,'add','WORK_REQUEST.md'); _git(root,'commit','-q','-m','Record customer work request')
    return root, _git(root,'rev-parse','HEAD')

def export_workspace(root, destination_base):
    return Path(shutil.make_archive(str(destination_base),'zip',root_dir=root))
