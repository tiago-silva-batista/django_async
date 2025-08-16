import asyncio
from django.http import HttpResponse

async def ds(request):
    numeros = []
    for i in range(1, 11):
        numeros.append(str(i))
        await asyncio.sleep(0.1)
    return HttpResponse("Contagem: " + " ".join(numeros))
