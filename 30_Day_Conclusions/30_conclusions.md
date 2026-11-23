<div align="center">

  <h1> 30 Days Of Python: Day 30- Conclusions</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>


<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 29](../29_Day_Building_API/29_building_API.md)
![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Day 30](#day-30)
  - [Conclusions](#conclusions)
  - [Testimony](#testimony)

# Day 30


## Conclusions

In the process of preparing this material I  have learned quite a lot and you have inspired me to do more. Congratulations for making it to this level. If you have done all the exercise and the projects, now you are capable to go to  a data analysis, data science, machine learning or web development paths. [Support the author for more educational materials](https://www.paypal.com/paypalme/asabeneh).

## Testimony
Now it is time to express your thoughts about the Author and 30DaysOfPython. You can leave your testimonial on this [link](https://www.asabeneh.com/testimonials)

## Added Activity: Applied Lab — Capstone Expense Summarizer (`R27-T021`)

> **Note:** This is an added applied activity and not an original numbered exercise.

- **Lab directory**: [`30_Day_Conclusions/applied-labs/r27-t021`](./applied-labs/r27-t021/README.md) ([`example.py`](./applied-labs/r27-t021/example.py))
- **Inputs**: Local CSV lines `food,12.50`, `food,7.50`, and `travel,5.00` (plus negative expense rows such as `food,-3.00` on line 2 to verify validation).
- **Expected result**: Valid category totals aggregate to `food=20.00` and `travel=5.00`, while invalid negative expenses are rejected and reported by their 1-based line number.
- **Verification command**:
  ```sh
  python3 -m unittest discover -s 30_Day_Conclusions/applied-labs/r27-t021 -p "test_*.py"
  ```

GIVE FEEDBACK:
http://thirtydayofpython-api.herokuapp.com/feedback

🎉 CONGRATULATIONS ! 🎉

[<< Day 29](../29_Day_Building_API/29_building_API.md)
