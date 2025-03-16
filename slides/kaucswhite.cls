% Beamer template for KAU CS white.
%
% By Tobias Pulls, based on the SINTEF template by Federico Zenith,
% federico.zenith@sintef.no. Derived (through several iterations) from Håvard
% Berland's beamerthementnu class.
%
% This program is free software: you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
% This program is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.
%
% You should have received a copy of the GNU General Public License
% along with this program.  If not, see <http://www.gnu.org/licenses/>.

\ProvidesClass{kaucsbrown}[2020/01/11]
\RequirePackage{etoolbox}
\newcommand{\@DashColor}{secondcolor}
\newcommand{\@DashHeight}{0.8mm}
\PassOptionsToClass{aspectratio=169}{beamer} % Default, may be overridden
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}
\ProcessOptions\relax
\LoadClass{beamer}
\usepackage{tikz}
\usepackage{caladea,carlito}
\usepackage{graphicx,ifthen,xcolor}
\usefonttheme[onlymath]{serif}
\renewcommand{\familydefault}{\sfdefault}

% main colors
\definecolor{maincolor}{HTML}{ffffff}
\definecolor{maincolorshade}{HTML}{bdae93}
\definecolor{secondcolor}{RGB}{89,49,107}
\definecolor{textcolor}{HTML}{282828}
%\definecolor{alertcolor}{HTML}{8f3f71}

% block colors
\definecolor{blocktitlebg}{HTML}{a89984}
\definecolor{blocktitlefg}{HTML}{282828}
\definecolor{blockbodybg}{HTML}{bdae93}
\definecolor{blockbodyfg}{HTML}{3c3836}

% Following commands will not be activated for article mode.
\mode<presentation>

% No navigation symbols
\setbeamertemplate{navigation symbols}{}

% Set colours
\setbeamercolor{alerted text}{fg=secondcolor}
\setbeamercolor{headline}{fg=textcolor,bg=maincolor}
\setbeamercolor{author}{fg=secondcolor}
\setbeamercolor{block title}{fg=blocktitlefg,bg=blocktitlebg}
\setbeamercolor{block body}{fg=blockbodyfg,bg=blockbodybg}
\setbeamercolor{normal text}{fg=textcolor}
\setbeamercolor{background canvas}{bg=maincolor}
\setbeamercolor{structure}{fg=textcolor}
\setbeamercolor{title}{fg=textcolor,bg=maincolor}
\setbeamercolor{footline}{fg=textcolor}
\setbeamercolor{itemize items}{fg=textcolor}
\setbeamerfont{description item}{series=\bfseries}

% Bullets in several levels
\setbeamertemplate{itemize item}{\textbullet}
\setbeamertemplate{itemize subitem}{\textendash}
\setbeamertemplate{itemize subsubitem}{\guillemotright}

% Define frame title and subtitle layout
\setbeamerfont{author}{size=\scriptsize}
\setbeamertemplate{frametitle}
{
\begin{beamercolorbox}[ht=15mm,dp=2mm]{frametitle}
    \usebeamerfont{frametitle}\insertframetitle\\
    \usebeamerfont{framesubtitle}\insertframesubtitle~\vphantom{phantomText}\\
    \textcolor{\@DashColor}{\rule[2ex]{1cm}{\@DashHeight}}
\end{beamercolorbox}
\vspace*{-0.65cm}
}

% Define the title page
\setbeamertemplate{title page}
{\vskip0pt plus 1filll\hfill
\pgfsetfillopacity{0.9}
\begin{beamercolorbox}[wd=85mm,sep=10pt,dp=0mm,left]{title}
    \usebeamerfont{title}\inserttitle

    \usebeamerfont{subtitle}\insertsubtitle
    
    \color{secondcolor}
    \vspace{2ex}
    \usebeamerfont{author}\textbf\insertauthor

    \color{textcolor}
    \vspace{0.25ex}
    \usebeamerfont{date}\insertdate
\end{beamercolorbox}
}

% Define the bottom of each standard frame
\setbeamerfont{footline}{size=\scriptsize}
\setbeamertemplate{footline}
{
  \begin{beamercolorbox}[wd=\textwidth,ht=4mm,dp=3mm]{footline}
    \usebeamerfont{footline}
    \hspace{2em}\insertframenumber
    \hfill
    \raisebox{-0.5ex}{\includegraphics[height=4ex]{kau}}
    \hspace{2em}
  \end{beamercolorbox}
}

\newcommand{\@TitleBackground}{default}
\newcommand{\titlebackground}{\renewcommand{\@TitleBackground}}
\renewcommand{\maketitle}{{% Double braces for local empty footline
  \graphicspath{{./backgrounds/}}
  \ifthenelse{\equal{\@TitleBackground}{}}{}{
    \usebackgroundtemplate{\includegraphics[width=\paperwidth,height=\paperheight]{\@TitleBackground}}
  }
  \setbeamertemplate{headline}{
  \hspace{0.074\textwidth}
  \begin{beamercolorbox}[center,wd=0.125\textwidth,ht=0.2675\textheight,dp=0mm]{headline}
    \raisebox{5mm}{\includegraphics[width=0.45\textwidth]{kau}}
  \end{beamercolorbox}
  }%
  \setbeamertemplate{footline}{}%
  \begin{frame}%
  \titlepage%
  \end{frame}%
  \addtocounter{framenumber}{-1}%
}}

\newcommand{\@finaltext}{Thank you, questions?}
\newcommand{\setmotto}{\renewcommand{\@finaltext}}
\newcommand{\backmatter}{
\setbeamercolor{background canvas}{bg=maincolor}
\begin{frame}[plain,c]
\begin{center}
  \textcolor{textcolor}{\@finaltext}
  
  \vspace{3ex}
  \includegraphics[height=5ex]{kau}
\end{center}
\end{frame}
}

\AtBeginSection{\frame{\sectionpage}}
\newdimen\slidewidth % auxiliary dimension
\newdimen\slideheight % auxiliary dimension
\slidewidth=\the\paperwidth
\slideheight=\the\paperheight
\setbeamertemplate{section page}
{
	\begin{tikzpicture}
		% set up the entire slide as the canvas
		\useasboundingbox (0,0) rectangle(\slidewidth,\slideheight);
		\fill[color=maincolor] (-1cm, 2cm) rectangle (\slidewidth, \slideheight+0.1cm);
		\fill[color=maincolor] (-1cm, 0.5\slideheight-1cm) rectangle(\slidewidth, 0.5\slideheight+1cm);
		\node[text width=\the\paperwidth-1cm,align=center] at (0.4\slidewidth, 0.5\slideheight) {\color{textcolor}\Huge\insertsection};
	\end{tikzpicture}
}

% make the itemize bullets pixelated >
\setbeamertemplate{itemize item}{
	\tikz{
		\draw[fill=blockbodyfg,draw=none] (0, 0) rectangle(0.1, 0.1);
		\draw[fill=blockbodyfg,draw=none] (0.1, 0.1) rectangle(0.2, 0.2);
		\draw[fill=blockbodyfg,draw=none] (0, 0.2) rectangle(0.1, 0.3);
	}
}
% make the subitems also pixelated >, but a little smaller and red
\setbeamertemplate{itemize subitem}{
	\tikz{
		\draw[fill=blocktitlebg,draw=none] (0, 0) rectangle(0.075, 0.075);
		\draw[fill=blocktitlebg,draw=none] (0.075, 0.075) rectangle(0.15, 0.15);
		\draw[fill=blocktitlebg,draw=none] (0, 0.15) rectangle(0.075, 0.225);
	}
}

\mode<all>

