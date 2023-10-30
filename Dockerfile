FROM archlinux:latest

RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm base-devel git sudo 
RUN pacman -Scc --noconfirm

RUN pacman -S --noconfirm texlive 
RUN pacman -S --noconfirm texlive-langeuropean

RUN pacman -S --noconfirm biber

WORKDIR /home/latex

COPY Naloga.tex ./Naloga.tex
COPY viri.bib ./viri.bib
COPY slike ./slike
COPY script.sh ./script.sh

RUN mkdir /output
CMD ["bash", "script.sh"]

# move Naloga.pdf to outside of container
# docker run -v /home/latex:/output <image_name>
