import json
import subprocess
import youtubesearchpython as yts


def search_phrase(phrase):

	try:
		search = yts.VideosSearch(str(phrase), limit=1)
		results = search.result()
		data = results['result'][0]

		half_dict = {}
		half_dict.update({'id': data['id'],'link': data['link'], 'song_title': data['title'], 'duration': data['duration']})
		save_dict = {data['id']: half_dict}
		vid_id = data['id']
		song_check(save_dict, vid_id)
		return data['link']

	except:
		print(f'Search Resulted in no matches for {phrase}')

def download_video(url):
	subprocess.run(f'yt-dlp -f "ba" -x --audio-format mp3 {url} -o "%(id)s.mp3"')

def song_check(to_write, video_id):
	dict_ids = load_ids()

	if str(video_id) in dict_ids:
		print('ID already in library')

	else:
		print('New ID, adding to library')
		write_song(to_write, video_id)

	return

def write_song(vd, video_id):
	songs = load_songs()
	songs.update(vd)
	with open('index.json', 'w', encoding='utf-8') as file:
		json.dump(songs, file, indent=4)
	return

def load_songs():
	with open('index.json', 'r', encoding='utf-8') as file:
		songs = json.load(file)
		return songs

def load_ids():
	with open('index.json', 'r', encoding='utf-8') as file:
		songs = json.load(file)
		song_ids = songs.keys()
		return song_ids

def play_song(q):
	song_data = search_phrase(q)
	download_video(song_data)


if __name__ == "__main__":
	play_song('plaza eric reprid')
