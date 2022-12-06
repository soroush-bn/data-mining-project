# data mining for [University Of Bern](https://www.unibe.ch/)
### introduction : 
In this project, we will go through all the courses in all faculties of Bern University, and we will 
fetch the **required data** for the next phase of project, in which useful data will be extracted.
___
### Phase one :
This phase is dedicated to **scraping** data from the  [course page]("https://www.ksl.unibe.ch/KSL/veranstaltungen?1/") by using a selenium crawler which can be found 
in [*crawler.py*](https://github.com/soroush-bn/data-mining-project/blob/main/Crawler.py).
Two methods were implemented for getting courses data:
1. looping through all faculties, then all courses of that faculty and getting necessary data from each coloumn.

    `def get_course_data(self, course):`

2. simply using the **download option** that website provided us :D.

    `def download_standard_report(self):`
___
### Phase two  :
This phase is dedicated to **preprocessing**,**keyword extraction** and **frequent pattern extraction**.
* Preprocessing : 
  * For a neat and clean data we need to embed usefull data of our previous section(e.g. outcome, objective, description and ...) and use some methods like
  stemming and lemmatizing and removing the stopwords of the embedded text.
  
* Keyword extraction :
  * with **BERT** method and using keyBERT library we extract the keywords of the preprocessed data.
  
* Frequent pattern extraction : 
  * there are some frequent pattern in keywords which have been fetched, so with using libraries like mltext we can find that keyword in this section.

___
### Phase three :
In this phase we have to **cluster** and **classify** the extracted keywords from the previous phase. 
In order to feed our methods with  numeric inputs we need to convert our keywords to numbers! for solving this conversion we use BERT method and libraries like Hugging Face or 
Sentence-Transformers.
Once converted the keywords to numeric vectors, data is ready to go through the final steps.
* Clustering :
  * for clustering the data, three approaches were used :
    1. KMeans
    2. DBScan
    3. AgglomerativeClustering
 * Classification : 
   * for classification again, three different classifier were used :
      1. DecisionTreeClassifier
      2. GaussianNB
      3. KNeighbors
 
