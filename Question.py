class Question:
	def __init__(self, question: str, answer: str) -> None:
		self.question = question
		self.answer = answer

	def json(self):
		return {
			"question": self.question,
			"answer": self.answer
		}
