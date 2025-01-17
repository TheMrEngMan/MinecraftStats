from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_junkfood',
        {
            'title': 'Bad Diet',
            'desc': 'Junkfood items eaten',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:rotten_flesh']),
            mcstats.StatReader(['minecraft:used','minecraft:spider_eye']),
            mcstats.StatReader(['minecraft:used','minecraft:poisonous_potato']),
        ])
    ))
