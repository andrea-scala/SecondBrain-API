#Scelgo l'immagine base di python
FROM python:3.11-slim
#Setto la workdir
WORKDIR /app
#Copio il file requirements.txt nella working dir
COPY requirements.txt ./ 
#Installo le dipendenze
RUN pip install --no-cache-dir -r requirements.txt
#Copio il codice
COPY . .
#Esporto la porta 8000
EXPOSE 8000
#Eseguo il comando per avviare l'applicazione
#0.0.0.0 è necessario perchè uvicorn di default ascolta solo sulla porta localhost, quindi non sarebbe accessibile dall'esterno del container.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]