# CVPR 2019 Accepted Papers

The main goal of these scripts is to build a page that displaying the accepted papers for CVPR 2019 in a way that is easier for humans to parse (re: https://mattdeitke.github.io/CVPR2019 ). Below is an example of what this repository will display and following that is what CVPR open access currently displays.

<img src="site.gif" style="width:100%"/>
<div style="text-align:center">
	<img src="oar_preview.png" style="width:60%;"/>
</div>
In particular, there is functionality to cluster papers based on latent Dirichlet allocation topics, create thumbnail images from the first 8 pages of each PDF, find the abstracts, copy a bibtex, view the paper and supplementary material, and more. Feel free to use the scripts as they are up to date with Python 3.7 and should work for any past CVPR (unless they change their HTML) as well as making modifications to adapt to another conference.

#### Installation

0. Clone this repository `git clone https://github.com/mattdeitke/CVPR-2019`

1. Save the HTML from where the accepted papers are displayed. For CVPR, this year, that would be `http://openaccess.thecvf.com/CVPR2019.py`.

2. Install ImageMagick, if it is not already installed. This can be done using `sudo apt-get install imagemagick` or using another supported method such as `brew install imagemagick`.

3. Run `pdftowordcloud.py` (to generate top words for each paper. Output saved in topwords.p as pickle)

4. Run `pdftothumbs.py` (to generate tiny thumbnails for all papers. Outputs saved in thumbs/ folder)

5. Run `scrape.py` (to generate paperid, title, authors list by scraping NIPS .html page)

6. Run `makecorpus.py` (to create allpapers.txt file that has all papers one per row)

7. Run `python lda.py -f allpapers.txt -k 7 --alpha=0.5 --beta=0.5 -i 100` . This will generate a pickle file called `ldaphi.p` that contains the LDA word distribution matrix. Thanks to this [nice LDA code](https://github.com/shuyo/iir/blob/master/lda/lda.py) by @shuyo! It requires nltk library and numpy. In this example we are using 7 categories. You would need to change the `nipsnice_template.html` file a bit if you wanted to try different number of categories.

8. Generate the abstract files inside abstracts/ folder using `getabstracts.py`.

9. Finally, run `generatenicelda.py` (to create the `index.html` page)

### Acknowledgements

Big thanks to @karpathy for his [NeurIPS preview](https://github.com/karpathy/nipspreview) and [ArXiV Sanity Preserver](https://github.com/karpathy/arxiv-sanity-preserver), which is what this repository is built on top of! Also a thanks to @tholman for creating a more modern [GitHub Corners](https://github.com/tholman/github-corners) and @shuyo for the [LDA code](https://github.com/shuyo/iir/blob/master/lda/lda.py)! Finally, more thanks go to the people at CVPR for [openly publishing all of their accepted papers](http://openaccess.thecvf.com/CVPR2019.py)!

#### Licence

WTFPL licence
