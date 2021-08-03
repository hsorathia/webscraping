from generator import HeartWork

print('hi')
gener = 'http://qalaminstitute.org/podcast/audio/surah_maryam_heartwork/heartwork_maryam_1.mp3'
idx = gener.rfind('/') + 1
title = gener[idx:]

gener = HeartWork('http://qalaminstitute.org/podcast/audio/surah_maryam_heartwork/heartwork_maryam_1.mp3', 20)
gener.begin()