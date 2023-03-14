<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h1 align="center">Enhancements to Adaptive Impedence Control in Anklebot</h1>


</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#demo">Demo</a></li>
      </ul>
    </li>
    <li>
      <a href="#report">Report</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#usage">Usage</a></li>
	<li><a href="#additional-information">Additional Information</a></li>
      </ul>
    </li>
    <li><a href="#contributors">Contributors</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


The use of rehabilitation robots, particularly Anklebots, is growing in post-stroke therapy as a response to the aging population and shortage of physiotherapists, with the aim of promoting patient participation.
This project deals with the validation of existing work on Anklebot [Main Paper](https://ieeexplore.ieee.org/document/8561224) and the efficacy of the enhancements we suggested.  

Summary of tasks achieved:
* An adaptive approach was compared with a fixed-stiffness approach using the Anklebot during patient-led movements, by synthetically generating virtual
ankle stiffness values of the human from main paper. 
* A **cost function** was modified to improve system performance by replacing L2 error with **L1 error** for adaptive stiffness calculation.
* **Force feedback control** was added to **reduce the apparent mass and friction** felt by the patient due to the robot.
* ```Proposed enhancement 1``` improved smoothness in motion by reducing sudden jerks in the dorsi-plantar flexion angle (θ).
* ```Proposed enhancement 2``` improved backdrivability by reducing the overall apparent mass and damping.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Demo

Anklebot setup | Control Diagram with Force Feedback
:-------------------------:|:-------------------------:
<img src="https://github.com/KACHAPPILLY2021/Computer_Vision_projects/blob/main/proj_1/texture.jpg?raw=true" width=40% alt="original"> | <img src="https://github.com/KACHAPPILLY2021/Computer_Vision_projects/blob/main/proj_1/output_1/2_main.PNG?raw=true" width=30% alt="reconstructed">

<div align="center">


  <h4 align="center"> Explorer and Follower working (X16 Speed)</h4>


</div>

https://user-images.githubusercontent.com/90359587/224387441-d45e0f85-1992-43dc-be13-360b4ef2d11c.mp4
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!--  Reports -->
## Report

Detailed report in IEEE format can be found [here](https://github.com/KACHAPPILLY2021/Ankle_bot/blob/main/ENPM640_Project_Report.pdf).
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

These are the instructions to get started on the project.
To get a local copy up and running follow these simple steps.

### Prerequisites
* atleast Python 3.6
* Libraries required : Scipy(odeint), Numpy, Matplolib 


### Usage

1. Clone repo and navigate to ```Ankle_bot``` directory.
   ```sh
   git clone https://github.com/KACHAPPILLY2021/Ankle_bot.git
   ```
2. To run the code for fixed stiffness:
   ```sh
   python3 fixed_stiffness.py
   ```
3. To run the code for adaptive stiffness:
   ```sh
   python3 adaptive_stiffness.py
   ```
4. To run the code for force feedback:
   ```sh
   python3 force_feedback.py
   ```
5. To run the code for enhancement 1 (New Cost function):
   ```sh
   python3 enhancement_1.py
   ```
### Additional Information

* All the parameters used in the code are in the file ```params.py``` in the [utils](https://github.com/KACHAPPILLY2021/Ankle_bot/tree/main/utils) folder.
* The results/plots are stored in the [Results](https://github.com/KACHAPPILLY2021/Ankle_bot/tree/main/Results) folder.
* This program is designed for any number of movements(going up and going down) i.e., dorsiflexions and plantarflexions
* To change the number of movements modify the ```n_movements``` parameter in the respective files as needed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTORS -->
## Contributors

- [Aditya Varadaraj](https://github.com/AdityaVaradaraj)
- [Jeffin Johny](https://github.com/KACHAPPILLY2021)
- Prateek Verma
- [Saurabh Palande](https://github.com/saurabhp369)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jeffin Johny K - [![MAIL](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jeffinjk@umd.edu)
	
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/KACHAPPILLY2021)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](http://www.linkedin.com/in/jeffin-johny-kachappilly-0a8597136)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [MIT](https://choosealicense.com/licenses/mit/) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
