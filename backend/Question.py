from typing import Optional


class Question:
	def __init__(
					self,
					question: str,
					answer: str,
					image_url: Optional[str] = None,
					image_alt: Optional[str] = None
	) -> None:
		self.question = question
		self.answer = answer
		self.image_url = image_url
		self.image_alt = image_alt

	def json(self):
		if self.image_url:
			return {
				"question": self.question,
				"answer": self.answer,
				"image_url": self.image_url,
				"image_alt": self.image_alt
			}

		return {
			"question": self.question,
			"answer": self.answer
		}
