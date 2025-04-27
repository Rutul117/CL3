import pandas as pd

def mapper(data):
    for temp, row in data.iterrows():
        year = row['date'][:4]
        yield (int(year), row['temp'])


def reducer(mapped_data):    
    year_temp_dict = {}
    for year, temp in mapped_data:
        if year not in year_temp_dict:
            year_temp_dict[year] = []
        year_temp_dict[year].append(temp)

    year_stats = {}
    for year, temps in year_temp_dict.items():
        max_temp = max(temps)
        min_temp = min(temps)
        avg_temp = sum(temps) / len(temps)
        year_stats[year] = {"max": max_temp, "min": min_temp, "avg": avg_temp}
    
    return year_stats


weather_data = pd.read_csv('/Users/rutulbhosale/Desktop/8 Semester/Practicals/CL-3/10/weather_data.csv')
mapped_data = list(map(mapper, [weather_data])) 
flattened_data = [] 
for sublist in mapped_data:
    for item in sublist:
        flattened_data.append(item)

year_stats = reducer(flattened_data)

for year, stats in year_stats.items():
    print(f"{year} : Max: {stats['max']:.1f}°C , Min: {stats['min']:.1f}°C , Avg: {stats['avg']:.2f}°C")