# live-translation
Translate the audio input using readily available machine learning tools and text-to-speech technology. 
This project is divided into parts, one stand alone Python script that collects the audio, translate and transfer the text to the web application.


```mermaid
  graph TD 
    A[Speaker] --> B[Auto Translator service] 
    B --> C[Web Application] 
    C --> D[Mobile devices]
```

## How does it work?

### Initialisation
The normal flow involves someone starting an live event and consequently generating a QR Code that points to the event.

### Access
Expectators interested in the translation of the event can scan the QR code and access the live translation.

### Broadcast
The Translator service will receive chunks of audio, translate then and transmit them to the Web Application and this one will broadcast to the connected expectators.

```mermaid
sequenceDiagram
    Administrator->>+WebApp: 1. Start event.
    WebApp->>WebApp: 2. Generate QR code.
    WebApp->>-Administrator: 3. QR code.
    Expectator->>+Expectator: 4. Scan QR code.
    Expectator->>-WebApp: 5. Access live translation (websocket).
    Presenter->>+AutoTranslator: 6. Live audio.
    AutoTranslator->>+WebApp: 7. Translation.
    WebApp->>-Expectator: 8. Translation.
```
