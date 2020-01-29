CANCELED = -10
ERROR = -5
NOT_CREATED = 0
IN_PROGRESS = 5
COMPLETED = 10
WAITING_DOWNLOAD = 15
BEING_DOWNLOADED = 20
BEING_PARSED = 25
PROCCESS_FINISHED = 30

STATUS_CREATION = (
    (CANCELED, 'Cancelado'),
    (ERROR, 'Erro no Scan'),
    (NOT_CREATED, 'não Criado'),
    (IN_PROGRESS, 'em Andamento'),
    (COMPLETED, 'Completo'),
    (WAITING_DOWNLOAD, 'Aguardando Dowload'),
    (BEING_DOWNLOADED, 'Baixando Scan'),
    (BEING_PARSED, 'Em Processamento'),
    (PROCCESS_FINISHED, 'Finalizado'),
)