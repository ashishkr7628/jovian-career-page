from flask import Flask, render_template,jsonify
print(__name__)

JOB= [
   {
      'id': 1,
      'position':"Software Developer",
      'location': "Bangalore, India",
      'salary': "Rs 10,00,000"

   },
   {
      'id': 2,
      'position':"Data Analyst",
      'location': "Bangalore, India",
      'salary': "Rs 15,00,000"

   },
   {
      'id': 3,
      'position':"Data Scientist",
      'location': "Bangalore, India",
      'salary': "Rs 10,00,000"

   },
   {
      'id': 4,
      'position':"Frontend Developer",
      'location': "Bangalore, India",
      'salary': "Rs 18,00,000"

   },
   {
      'id': 5,
      'position':"Backend Developer",
      'location': "Remote",


   }



]

app= Flask(__name__)

@app.route('/')

def Hello_World():
    return render_template('home.html',jobs=JOB)

@app.route('/api/jobs')

def jobs():
   return jsonify(JOB)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
 