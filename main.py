def dmr(nummer, deler):
  deler = int(deler)
  nummer = int(nummer)
  ateller = 1
  ateller = int(ateller)
  rbereken = deler
  rbereken = int(rbereken)
  while rbereken <= nummer:
      rbereken = rbereken + deler
      ateller = ateller + 1
  if rbereken > nummer:
      rbereken = rbereken - deler
      ateller = ateller - 1
      rest = nummer - rbereken
  print ("Rest:", rest)
  print ("Antwoord:", ateller)