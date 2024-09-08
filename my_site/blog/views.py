import logging

# Настройка логирования
logging.basicConfig(filename='debug.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def home(request):
    logger.debug("Вызов представления home")
    context = {
        'posts': Post.objects.all()
    }
    logger.debug("Контекст в home: %s", context)
    return render(request, 'blog/home.html', context)

def about(request):
    logger.debug("Вызов представления about")
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})
