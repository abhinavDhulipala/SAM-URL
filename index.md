## SAM URL (Tiny-url clone made with flask and AWS Lambda!!)
This guide will take you through a common interview question and is heavily inspired by a [this educative system interview design article](https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR)

### The Problem
URL shortening is a service to create an alias from a reall long url to a shorter one i.e: https://www.google.com/maps/place/Stanford+University/@37.4249706,-122.1878931,14z/data=!4m8!1m2!2m1!1sstanford!3m4!1s0x0:0x29cdf01a44fc687f!8m2!3d37.4274762!4d-122.1697176 -> http://tinyurl.com/<short-hash>. Short links are used to save space in loads of character limited text boxes like twitter, job applications, printed message boards. Especially if the message board is printed, people are less likely to erroneously enter the url into their browsers.

### Requirements

   #### Functional
   1. Given a url, our service should create a shorter url that performs a 302(redirect) to the original, longer url.
   
   #### Non-functional (Performance!!)
   1. Our service should be highly available. At any given moment in time, a user should be able to call our redirect link and be able to get a redirect. If our service is down, a whole lot of peoples redirects will start failing instantly. This means we need a really reliable service that we know won't crash under strenuous loads or have periodic maintenence times, etc.
   2. URL redirection needs to happen in real-time and really quickly. Always. Regardless of the type of machine we call it on or how many people are concurrently calling the same link, we should be able to get to our original url really quickly (within about 1/2 a second would be nice).
   3. We shouldn't have collisions in our link (every link should be unique and not guessable)
 

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/abhinavDhulipala/CLurKel/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
