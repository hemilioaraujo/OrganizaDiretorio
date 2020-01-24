import os, shutil
from pathlib import Path

path = Path('.')
suffixes = list({filepath.suffix[1:] for filepath in path.glob('*')})

print(suffixes)
print(path)

def cria_pastas(suffixes):
	for suffix in suffixes:
		if suffix != '':
			os.mkdir(Path('.')/f'{suffix}')


def get_itens_por_tipo(suffix):
    itens = list(Path('.').glob(f'*.{suffix}'))
    #print(itens)
    return itens


def move_itens(suffixes):
    for suffix in suffixes:
        if suffix != '':
            print(get_itens_por_tipo(suffix))
            itens = get_itens_por_tipo(suffix)
            for item in itens:
                src = item
                dst = Path('.')/f'{suffix}'
                src = os.fspath(src)
                if src != 'organiza.py':
                    dst = os.fspath(dst)
                    print(f'Origem: -> {src}\nDestino: -> {dst}')
                    shutil.move(src, dst)


cria_pastas(suffixes)
move_itens(suffixes)