class Question:

    def __init__( self , q_text , q_answer ):
        self.text   = self.reformat_text( q_text )
        self.answer = q_answer

    def reformat_text( self , text : str ):
        formatted_text = text.replace('&quot;', '"')
        formatted_text = formatted_text.replace('&#039;', "'")
        formatted_text = formatted_text.replace('&rsquo;', "'")
        return formatted_text
