def transcribe(file, requestedModel, task, output, language):
    model = whisper.load_model(requestedModel)

    return model.transcribe(file.name, language=language, task=task)