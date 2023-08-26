import modules.scraping as scraper

def getSubjectCode():
  url = 'http://repository.lppm.unila.ac.id/view/subjects/'

  scrap_result = scraper.parsePage(scraper.getDriver(), url)
  cat = scraper.getSubjectsLink(scrap_result, '#content > div > ul > li > ul > li > ul > li > a')

  return cat

def getSubSubjectCode():
  url = 'http://repository.lppm.unila.ac.id/view/subjects/'

  scrap_result = scraper.parsePage(scraper.getDriver(), url)
  cat = scraper.getSubjectsLink(scrap_result, '#content > div > ul > li > ul > li > ul > li > ul > li > a')

  return cat

def mergedSortedSubject():
  subSubject = getSubSubjectCode()
  Subject = getSubjectCode()
  mergedSubject = subSubject + Subject
  mergedSorted = sorted(mergedSubject)

  return mergedSorted

#content > div > ul > li > ul > li > ul > li > a