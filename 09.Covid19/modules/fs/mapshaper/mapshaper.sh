mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^11.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Seoul.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^26.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Busan.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^27.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Daegu.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^28.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Incheon.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^29.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Gwangju.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^30.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Daejeon.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^31.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Ulsan.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^39.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Sejong.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^41.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Gyeonggi.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^42.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Gangwon.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^43.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Chungcheongbuk.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^44.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Chungcheongnam.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^45.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Jeollabuk.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^46.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Jeollanam.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^47.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Gyeongsangbuk.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^48.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Gyeongsangnam.json

mapshaper ./data/SIG_202005/SIG.shp encoding=euc-kr \
-proj wgs84 \
-filter '/^50.*/.test(SIG_CD)' \
-o format=geojson \
./data/SIG_202005/SIG-Jeju.json

