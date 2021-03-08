from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_dirt',
        {
            'title': 'Getting Dirty',
            'desc': 'Dirt blocks placed',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:dirt'])
    ))
