# File che utilizzeremo in futuro :D
from dao.filmDao import Film

result = Film.get_all_movies_belong_category()
print(result)
