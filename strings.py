theoryFilesDict = {
    "theoryChapter0": ["PDD2023", "ПДД-2023, вся теория"],
    "theoryChapter1": ["Obshchie_polozheniya", "Общие положения"],
    "theoryChapter2": ["Obshchie_obyazannosti_voditelej", "Общие обязанности водителей"],
    "theoryChapter3": ["Primenenie_specialnyh_signalov", "Применение специальных сигналов"],
    "theoryChapter4": ["Obyazannosti_peshekhodov", "Обязанности пешеходов"],
    "theoryChapter5": ["Obyazannosti_passazhirov", "Обязанности пассажиров"],
    "theoryChapter6": ["Signaly_svetofora_i_regulirovshchika", "Сигналы светофора и регулировщика"],
    "theoryChapter7": ["Primenenie_avarijnoj_signalizacii_i_znaka_avarijnoj_ostanovki", "Применение аварийной сигнализации и знака аварийной остановки"],
    "theoryChapter8": ["Nachalo_dvizheniya_i_manevrirovanie", "Начало движения, маневрирование"],
    "theoryChapter9": ["Raspolozhenie_transportnyh_sredstv_na_proezzhej_chasti", "Расположение транспортных средств на проезжей части"],
    "theoryChapter10": ["Skorost_dvizheniya", "Скорость движения"],
    "theoryChapter11": ["Obgon_operezhenie_vstrechnyj_razezd", "Обгон, опережение, встречный разъезд"],
    "theoryChapter12": ["Ostanovka_i_stoyanka", "Остановка и стоянка"],
    "theoryChapter13": ["Proezd_perekrestkov", "Проезд перекрестков"],
    "theoryChapter14": ["Peshekhodnye_perekhody_i_mesta_ostanovok", "Пешеходные переходы и места остановок маршрутных транспортных средств"],
    "theoryChapter15": ["Dvizhenie_cherez_zheleznodorozhnye_puti", "Движение через железнодорожные пути"],
    "theoryChapter16": ["Dvizhenie_po_avtomagistralyam", "Движение по автомагистралям"],
    "theoryChapter17": ["Dvizhenie_v_zhilyh_zonah", "Движение в жилых зонах"],
    "theoryChapter18": ["Prioritet_marshrutnyh_transportnyh_sredstv", "Приоритет маршрутных транспортных средств"],
    "theoryChapter19": ["Polzovanie_vneshnimi_svetovymi_priborami_i_zvukovymi_signalami","Пользование внешними световыми приборами и звуковыми сигналами"],
    "theoryChapter20": ["Buksirovka_mekhanicheskih_transportnyh_sredstv","Буксировка механических транспортных средств"],
    "theoryChapter21": ["Uchebnaya_ezda", "Учебная езда"],
    "theoryChapter22": ["Perevozka_lyudej", "Перевозка людей"],
    "theoryChapter23": ["Perevozka_gruzov", "Перевозка грузов"],
    "theoryChapter24": ["Velosipedisty_i_voditeli_mopedov", "Дополнительные требования к движению велосипедистов и водителей мопедов"],
    "theoryChapter25": ["guzhevye_povozki_i_progon_zhivotnyh", "Дополнительные требования к движению гужевых повозок, а также к прогону животных"]
}

def getBiletsCallBack():
    callBack = []
    for i in range(0,21):
        callBack.append(f'biletAB{i}')
    return callBack