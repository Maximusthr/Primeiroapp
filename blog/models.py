from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=200
    )
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, 
        null=True
    )
    def publish(self):
        self.published_date = timezone.now()
        self.save()  
    def __str__(self):
        return self.title

class Enxadrista(models.Model): # Enxadristas vivos
    nome = models.CharField(
        max_length=45
    )
    idade = models.PositiveIntegerField()
    pais = models.CharField(
        max_length=50,
        null = True,
        blank = True
    )
    Grande_Mestre = 'GM'
    Mestre_Internacional = 'MI'
    Mestre_Fide = 'MI'
    Candidato_a_Mestre = 'CM'
    Mestre_Nacional = 'MN'
    grupos = (
        (Grande_Mestre, 'Grande Mestre'),
        (Mestre_Internacional, 'Mestre Internacional'),
        (Mestre_Fide, 'Mestre FIDE'),
        (Candidato_a_Mestre, 'Candidato a Mestre'),
        (Mestre_Nacional, 'Mestre Nacional')
    )
    titulo = models.CharField(
        max_length=2,
        choices = grupos,
        null = True
    ) # Classificação segundo a FIDE
    rating = models.CharField(
        max_length=4,
        null = True,
        blank = True
    ) # Pontuação seguindo a FIDE
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return self.nome
    def publish(self):
        self.published_date = timezone.now()
        self.save()  

class JogadoresFavorito(models.Model):
    titulo = models.CharField(
        max_length=250,
        blank=True,
        default='Jogador(a)'
    )
    jogador = models.ForeignKey(
        Enxadrista,
        related_name='jogador_favorito',
        on_delete=models.CASCADE,
        null=True
    )
    motivo = models.CharField(
        max_length=550
    )
    def __str__(self):
        return self.titulo