def generator(text, sep=" ", option=None):
   if type(text) is not str or (option not in ['shuffle', 'unique', 'ordered'] and option is not None):
       yield "ERROR"
       return
   if option is None:
       for word in text.split(sep):
           yield word

