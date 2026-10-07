
#STATIC METHODS are those that doesnt require obj creation
class ChaiUtils:
    
    @staticmethod
    def CleanIngredients(text):
        return [item.strip() for item in text.split(",")]


raw = "water  ,milk   ,ginger"
# obj = ChaiUtils()
# print(obj.CleanIngredients(raw))        

cleaned = ChaiUtils.CleanIngredients(raw)
print(cleaned)
