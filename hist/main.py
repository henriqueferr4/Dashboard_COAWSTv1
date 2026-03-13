# ---- #
# Gerar e atualizar diretórios com histórico de plots
# ---- #

from datetime import datetime, timedelta #Data automatizada
from pathlib import Path
import shutil

data_atual = datetime.now().strftime("%Y%m%d")


# Remover diretório mais antigo que 9 dias 
def limpar_diretorios_antigos(dias=9, hoje = datetime.now()):
    base_dir = Path(__file__).resolve().parents[1] / "hist"

    print ("🔍 Limpando plots antigos 🔍")

    if not base_dir.exists():
        print("✅ Nenhum diretório histórico encontrado")
        return

    for pasta in base_dir.iterdir():
        if pasta.is_dir():
            try:
                data_pasta = datetime.strptime(pasta.name, "%Y%m%d")
                if (hoje - data_pasta).days > dias:
                    shutil.rmtree(pasta)
                    print ("♻️ Figuras antigas foram removidas!")
            except ValueError:
                pass

# Criar diretório do dia atual
def creat_dir(var):
    dir_plots = Path(f'/home/CIEX/COAWST_PREVISAO_OPR/{var}')
    dir_data = Path(__file__).resolve().parents[1] / "hist" / f"{data_atual}" / f"{var}"
    dir_data.mkdir(parents=True, exist_ok=True)

    for arquivo in dir_plots.iterdir():
        if arquivo.is_file():
            shutil.copy2(arquivo,  dir_data / arquivo.name) # copia arquivos para a página histórica

creat_dir("CHUVA")
creat_dir("Ondas")
creat_dir("Vento_850hPa")

limpar_diretorios_antigos()