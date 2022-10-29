class Question:
	def __init__(self, question: str, answer: str, image_url: str = None) -> None:
		self.question = question
		self.answer = answer
		self.image_url = image_url

	def json(self):
		if self.image_url:
			return {
				"question": self.question,
				"question_image_url": self.image_url,
				"answer": self.answer
			}

		return {
			"question": self.question,
			"answer": self.answer
		}
