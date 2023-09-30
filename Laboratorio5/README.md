### Notas sobre el Lab.

Este laboratorio se basa en el cosumo de la API de TMDB: https://developer.themoviedb.org/docs
Para efectos de laboratorio, se hizo un llamado al API para consumir las primeras 500 películas de la lista utiliando un URL con este formato: https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}", donde el movie_id varía de 0 a 499.

Los datos obtenidos se procesaron de acuerdo a lo solicitado y se colocaron en un diccionario anidado. Estos datos posteriormente se utilizaron para crear un Datafame en Pandas y así poder extraer la información deseada para ser graficada en Matplotlib.

Se ha utilizado threading para reducir el tiempo total del proceso de 100 s a 31 s.