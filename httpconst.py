#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date of version: 9/dic/2017 (G. C.)
# The Rainbow Dash HTTP Daemon Server
# Copyright © 2017 Giovanni Alfredo Garciliano Díaz

# This file is part of rdhttpd
# rdhttpd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# rdhttpd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with rdhttpd.  If not, see <http://www.gnu.org/licenses/>.

statuscodes = {
	("100", "Continue"),
	("101", "Switching Protocols"),
	("102", "Processing"),
	("103", "Checkpoint"),
	("200", "OK"),
	("201", "Created"),
	("202", "Accepted"),
	("203", "Non-Authoritative Information"),
	("204", "No Content"),
	("205", "Reset Content"),
	("206", "Partial Content"),
	("207", "Multi-Status"),
	("208", "Already Reported"),
	("300", "Multiple Choices"),
	("301", "Moved Permanently"),
	("302", "Found"),
	("303", "See Other"),
	("304", "Not Modified"),
	("305", "Use Proxy"),
	("306", "Switch Proxy"),
	("307", "Temporary Redirect"),
	("308", "Permanent Redirect"),
	("400", "Bad Request"),
	("401", "Unauthorized"),
	("402", "Payent Required"),
	("403", "Forbidden"),
	("404", "Not Found"),
	("405", "Method Not Allowed"),
	("406", "Not Acceptable"),
	("407", "Proxy Authentication Required"),
	("408", "Request Timeout"),
	("409", "Conflict"),
	("410", "Gone"),
	("411", "Lenght Required"),
	("412", "Precondition Failed"),
	("413", "Request Entity Too Large"),
	("414", "Request-URI Too Long"),
	("415", "Unsupported Media Type"),
	("416", "Request Range Not Sastifable"),
	("417", "Expectation Failed"),
	("418", "I'm a teapot"),
	("422", "Unprocessable Entity"),
	("423", "Locked"),
	("424", "Failed Dependency"),
	("426", "Upgrade Required"),
	("428", "Precondition Required"),
	("429", "Too Many Requests"),
	("431", "Request Header Fields Too Large"),
	("451", "Unavailable For Legal Reasons"),
	("500", "Internal Server Error"),
	("501", "Not Implemented"),
	("502", "Bad Gateway"),
	("503", "Service Unavailable"),
	("504", "Gateway Timeout"),
	("505", "HTTP Version Not Supported"),
	("506", "Variant Also Negotiates"),
	("507", "Insufficient Storage"),
	("508", "Loop Detected"),
	("509", "Bandwith Limit Exceeded"),
	("510", "Not Extended"),
	("511", "Network Authentication Required"),
}

iso639 = [
	"aa", # afar
	"ab", # abjasio
	"ae", # avéstico
	"af", # afrikáans
	"ak", # akano
	"am", # amhárico
	"an", # aragonés
	"ar", # árabe
	"as", # asanés
	"av", # avar
	"ai", # aimara
	"az", # azerí
	"ba", # baskir
	"be", # bielorruso
	"bg", # búlgaro
	"bh", # bhoyapurí
	"bi", # bislama
	"bm", # bambara
	"bn", # bengalí
	"bo", # tibetano
	"br", # bretón
	"bs", # bosnio
	"ca", # catalán
	"ce", # checheno
	"ch", # chamorro
	"co", # corso
	"cr", # cree
	"cs", # checo
	"cu", # eslavo eclesiástico antiguo
	"cv", # chuvasio
	"cy", # galés
	"da", # danes
	"de", # alemán
	"dv", # maldivo
	"dz", # dzongkha
	"ee", # ewé
	"el", # griego moderno
	"en", # inglés
	"eo", # esperanto
	"es", # español
	"et", # estonio
	"eu", # euskera
	"fa", # persa
	"ff", # fula
	"fi", # finés
	"fj", # fiyiano
	"fo", # feroés
	"fr", # francés
	"fy", # frisón
	"ga", # irlandés
	"gd", # gaélico
	"gl", # gallego
	"gn", # guaraní
	"gu", # guyaratí
	"gv", # manés
	"ha", # hausa
	"he", # hebreo
	"hi", # hindi
	"ho", # hiri motu
	"hr", # croata
	"ht", # haitiano
	"hu", # húngaro
	"hy", # armenio
	"hz", # herero
	"ia", # interlingua
	"id", # indonesio
	"ie", # occidental
	"ig", # igbo
	"ii", # yi de Sichuán
	"ik", # iñupiaq
	"io", # ido
	"is", # islandés
	"it", # italiano
	"iu", # inuktitut
	"ja", # japonés
	"jv", # javanés
	"ka", # georgiano
	"kg", # kongo
	"ki", # kikuyu
	"kj", # kuanyama
	"kk", # kazajo
	"kl", # groelandés
	"km", # camboyano
	"kn", # canarés
	"ko", # coreano
	"kr", # kanuri
	"ks", # cachemiro
	"ku", # kurdo
	"kv", # komi
	"kw", # córmico
	"ky", # kirguís
	"la", # latín
	"lb", # luxemburgués
	"lg", # luganda
	"li", # limburgués
	"ln", # lingala
	"lo", # lao
	"lt", # lituano
	"lu", # luba-katanga
	"lv", # letón
	"mg", # malgache
	"mh", # marshalés
	"mi", # maorí
	"mk", # macedonio
	"ml", # malayalam
	"mn", # mongol
	"mr", # maratí
	"ms", # malayo
	"mt", # maltés
	"my", # birmano
	"na", # nauruano
	"nb", # noruego bokmål
	"nd", # ndebele del norte
	"ne", # nepalí
	"ng", # ndonga
	"nl", # neerlandés
	"nn", # nynorsk
	"no", # noruego
	"nr", # ndelebe del sur
	"nv", # navajo
	"ny", # chichewa
	"oc", # occitano
	"oj", # ojibwa
	"om", # oromo
	"or", # oriya
	"os", # osético
	"pa", # panyabí
	"pi", # pali
	"pl", # polaco
	"ps", # pastú
	"pt", # portugués
	"qu", # quechua
	"rm", # romanche
	"rn", # kirundi
	"ro", # rumano
	"ru", # ruso
	"rw", # ruandés
	"sa", # sánscrito
	"sc", # sardo
	"sd", # sindhi
	"se", # sami septentrional
	"sg", # sango
	"si", # cingalés
	"sk", # eslovaco
	"sl", # eslovenio
	"sm", # samoano
	"sn", # shona
	"so", # somalí
	"sq", # albanés
	"sr", # serbio
	"ss", # suazi
	"st", # seshoto
	"su", # sundanés
	"sv", # sueco
	"sw", # suajili
	"ta", # tamil
	"te", # tégulu
	"tg", # tayiko
	"th", # tailandés
	"ti", # tigriña
	"tk", # turcomano
	"tl", # tagalo
	"tn", # setsuana
	"to", # tongano
	"tr", # turco
	"ts", # tsonga
	"tt", # tártaro
	"tw", # twi
	"ty", # tahitiano
	"ug", # uigur
	"uk", # ucraniano
	"ur", # urdu
	"uz", # uzbeko
	"ve", # venda
	"vi", # vietnamita
	"vo", # volapük
	"wa", # valón
	"wo", # wolof
	"xh", # xhosa
	"yi", # yiddish
	"yo", # yoruba
	"za", # chuan
	"zh", # chino
	"zu", # zulú
]
iso3166 = [
	"AF",  # Afganistán
	"AX",  # Åland, Islas
	"AL",  # Albania
	"DE",  # Alemania
	"AD",  # Andorra
	"AO",  # Angola
	"AI",  # Anguila
	"AQ",  # Antártida
	"AG",  # Antigua y Barbuda
	"SA",  # Arabia Saudita
	"DZ",  # Argelia
	"AR",  # Argentina
	"AM",  # Armenia
	"AW",  # Aruba
	"AU",  # Australia
	"AT",  # Austria
	"AZ",  # Azerbaiyán
	"BS",  # Bahamas (las)
	"BD",  # Bangladesh
	"BB",  # Barbados
	"BH",  # Bahrein
	"BE",  # Bélgica
	"BZ",  # Belice
	"BJ",  # Benin
	"BM",  # Bermudas
	"BY",  # Belarús
	"BO",  # Bolivia (Estado Plurinacional de)
	"BQ",  # Bonaire, San Eustaquio y Saba
	"BA",  # Bosnia y Herzegovina
	"BW",  # Botswana
	"BR",  # Brasil
	"BN",  # Brunei Darussalam
	"BG",  # Bulgaria
	"BF",  # Burkina Faso
	"BI",  # Burundi
	"BT",  # Bhután
	"CV",  # Cabo Verde
	"KH",  # Camboya
	"CM",  # Camerún
	"CA",  # Canadá
	"QA",  # Qatar
	"TD",  # Chad
	"CL",  # Chile
	"CN",  # China
	"CY",  # Chipre
	"CO",  # Colombia
	"KM",  # Comoras (las)
	"KP",  # Corea (la República Popular Democrática de)
	"KR",  # Corea (la República de)
	"CI",  # Côte d'Ivoire
	"CR",  # Costa Rica
	"HR",  # Croacia
	"CU",  # Cuba
	"CW",  # Curaçao
	"DK",  # Dinamarca
	"DM",  # Dominica
	"EC",  # Ecuador
	"EG",  # Egipto
	"SV",  # El Salvador
	"AE",  # Emiratos Árabes Unidos (los)
	"ER",  # Eritrea
	"SK",  # Eslovaquia
	"SI",  # Eslovenia
	"ES",  # España
	"US",  # Estados Unidos de América (los)
	"EE",  # Estonia
	"ET",  # Etiopía
	"PH",  # Filipinas (las)
	"FI",  # Finlandia
	"FJ",  # Fiji
	"FR",  # Francia
	"GA",  # Gabón
	"GM",  # Gambia (la)
	"GE",  # Georgia
	"GH",  # Ghana
	"GI",  # Gibraltar
	"GD",  # Granada
	"GR",  # Grecia
	"GL",  # Groenlandia
	"GP",  # Guadeloupe
	"GU",  # Guam
	"GT",  # Guatemala
	"GF",  # Guayana Francesa
	"GG",  # Guernsey
	"GN",  # Guinea
	"GW",  # Guinea Bissau
	"GQ",  # Guinea Ecuatorial
	"GY",  # Guyana
	"HT",  # Haití
	"HN",  # Honduras
	"HK",  # Hong Kong
	"HU",  # Hungría
	"IN",  # India
	"ID",  # Indonesia
	"IQ",  # Iraq
	"IR",  # Irán (República Islámica de)
	"IE",  # Irlanda
	"BV",  # Bouvet, Isla
	"IM",  # Isla de Man
	"CX",  # Navidad, Isla de
	"IS",  # Islandia
	"KY",  # Caimán, (las) Islas
	"CC",  # Cocos / Keeling, (las) Islas
	"CK",  # Cook, (las) Islas
	"FO",  # Feroe, (las) Islas
	"GS",  # Georgia del Sur (la) y las Islas Sandwich del Sur
	"HM",  # Heard (Isla) e Islas McDonald
	"FK",  # Malvinas [Falkland], (las) Islas
	"MP",  # Marianas del Norte, (las) Islas
	"MH",  # Marshall, (las) Islas
	"PN",  # Pitcairn
	"SB",  # Salomón, Islas
	"TC",  # Turcas y Caicos, (las) Islas
	"UM",  # Islas Ultramarinas Menores de los Estados Unidos (las)
	"VG",  # Vírgenes británicas, Islas
	"VI",  # Vírgenes de los Estados Unidos, Islas
	"IL",  # Israel
	"IT",  # Italia
	"JM",  # Jamaica
	"JP",  # Japón
	"JE",  # Jersey
	"JO",  # Jordania
	"KZ",  # Kazajstán
	"KE",  # Kenya
	"KG",  # Kirguistán
	"KI",  # Kiribati
	"KW",  # Kuwait
	"LA",  # Lao, (la) República Democrática Popular
	"LS",  # Lesotho
	"LV",  # Letonia
	"LB",  # Líbano
	"LR",  # Liberia
	"LY",  # Libia
	"LI",  # Liechtenstein
	"LT",  # Lituania
	"LU",  # Luxemburgo
	"MO",  # Macao
	"MK",  # Macedonia (la ex República Yugoslava de)
	"MG",  # Madagascar
	"MY",  # Malasia
	"MW",  # Malawi
	"MV",  # Maldivas
	"ML",  # Malí
	"MT",  # Malta
	"MA",  # Marruecos
	"MQ",  # Martinique
	"MU",  # Mauricio
	"MR",  # Mauritania
	"YT",  # Mayotte
	"MX",  # México
	"FM",  # Micronesia (Estados Federados de)
	"MD",  # Moldova (la República de)
	"MC",  # Mónaco
	"MN",  # Mongolia
	"ME",  # Montenegro
	"MS",  # Montserrat
	"MZ",  # Mozambique
	"MM",  # Myanmar
	"NA",  # Namibia
	"NR",  # Nauru
	"NP",  # Nepal
	"NI",  # Nicaragua
	"NE",  # Níger (el)
	"NG",  # Nigeria
	"NU",  # Niue
	"NF",  # Norfolk, Isla
	"NO",  # Noruega
	"NC",  # Nueva Caledonia
	"NZ",  # Nueva Zelandia
	"OM",  # Omán
	"NL",  # Países Bajos (los)
	"PK",  # Pakistán
	"PW",  # Palau
	"PS",  # Palestina, Estado de
	"PA",  # Panamá
	"PG",  # Papua Nueva Guinea
	"PY",  # Paraguay
	"PE",  # Perú
	"PF",  # Polinesia Francesa
	"PL",  # Polonia
	"PT",  # Portugal
	"PR",  # Puerto Rico
	"GB",  # Reino Unido de Gran Bretaña e Irlanda del Norte (el)
	"EH",  # Sahara Occidental
	"CF",  # República Centroafricana (la)
	"CZ",  # República Checa (la)
	"CG",  # Congo (el)
	"CD",  # Congo (la República Democrática del)
	"DO",  # Dominicana, (la) República
	"RE",  # Reunión
	"RW",  # Rwanda
	"RO",  # Rumania
	"RU",  # Rusia, (la) Federación de
	"WS",  # Samoa
	"AS",  # Samoa Americana
	"BL",  # Saint Barthélemy
	"KN",  # Saint Kitts y Nevis
	"SM",  # San Marino
	"MF",  # Saint Martin (parte francesa)
	"PM",  # San Pedro y Miquelón
	"VC",  # San Vicente y las Granadinas
	"SH",  # Santa Helena, Ascensión y Tristán de Acuña
	"LC",  # Santa Lucía
	"ST",  # Santo Tomé y Príncipe
	"SN",  # Senegal
	"RS",  # Serbia
	"SC",  # Seychelles
	"SL",  # Sierra leona
	"SG",  # Singapur
	"SX",  # Sint Maarten (parte neerlandesa)
	"SY",  # República Árabe Siria
	"SO",  # Somalia
	"LK",  # Sri Lanka
	"SZ",  # Swazilandia
	"ZA",  # Sudáfrica
	"SD",  # Sudán (el)
	"SS",  # Sudán del Sur
	"SE",  # Suecia
	"CH",  # Suiza
	"SR",  # Suriname
	"SJ",  # Svalbard y Jan Mayen
	"TH",  # Tailandia
	"TW",  # Taiwán (Provincia de China)
	"TZ",  # Tanzania, República Unida de
	"TJ",  # Tayikistán
	"IO",  # Territorio Británico del Océano Índico (el)
	"TF",  # Tierras Australes Francesas (las)
	"TL",  # Timor-Leste
	"TG",  # Togo
	"TK",  # Tokelau
	"TO",  # Tonga
	"TT",  # Trinidad y Tabago
	"TN",  # Túnez
	"TM",  # Turkmenistán
	"TR",  # Turquía
	"TV",  # Tuvalu
	"UA",  # Ucrania
	"UG",  # Uganda
	"UY",  # Uruguay
	"UZ",  # Uzbekistán
	"VU",  # Vanuatu
	"VA",  # Vaticano, Ciudad del
	"VE",  # Venezuela (República Bolivariana de)
	"VN",  # Viet Nam
	"WF",  # Wallis y Futuna
	"YE",  # Yemen
	"DJ",  # Djibouti
	"ZM",  # Zambia
	"ZW",  # Zimbabwe
]
