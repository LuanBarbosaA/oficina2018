from django.db import models


class Times(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Time")
    pvencidas = models.IntegerField(null=True, verbose_name="Partidas vencidas")
    pperdidas = models.IntegerField(null=True, verbose_name="Partidas perdidas")
    pjogadas = models.IntegerField(null=True, verbose_name="Partidas jogadas")

    def __str__(self):
        return self.nome


class Usuarios(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome completo")
    email = models.EmailField(max_length=100, verbose_name="E-mail")
    senha = models.CharField(max_length=100, verbose_name="Senha")
    sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    idade = models.DateField(verbose_name="Data de nascimento")
    criado_em = models.DateTimeField(auto_now=True)
    fk_times = models.ForeignKey(Times, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome


class Locais(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do local")
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=150)
    ESTADOS = (
        ('MG', 'Minas Gerais'),
        ('SP', 'São Paulo'),
        ('AC', 'Acre'),
        ('ES', 'Espirito Santo'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('GO', 'Goias'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField(choices=ESTADOS, max_length=2)
    valor_aluguel = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name="Valor do aluguel")

    def __str__(self):
        return self.nome


class Partidas(models.Model):
    # nome = models.CharField()
    inicio_partida = models.DateTimeField(verbose_name="Data e hora do inicio da partida")
    fim_partida = models.DateTimeField(verbose_name="Data e hora do fim da partida")
    placar1 = models.IntegerField(verbose_name="Placar do time 1")
    placar2 = models.IntegerField(verbose_name="Placar do time 2")
    time1 = models.ForeignKey(Times, related_name="time1", on_delete=models.PROTECT)
    time2 = models.ForeignKey(Times, related_name="time2", on_delete=models.PROTECT)
    local = models.ForeignKey(Locais, on_delete=models.PROTECT)

    # lances = models.ForeignKey(Lances, on_delete=models.PROTECT)

    @property
    def nome(self):
        if (self.time1 and self.time2):
            return self.time1.nome + ' vs ' + self.time2.nome
        else:
            return 'Sem times definidos'


class Lances(models.Model):
    tipo_lance = models.CharField(max_length=150, verbose_name="Tipo do lance")
    data_lance = models.DateTimeField(verbose_name="Data e hora do lance")
    usuario = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    partida = models.ForeignKey(Partidas, on_delete=models.PROTECT)
