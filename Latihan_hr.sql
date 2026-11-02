-- Database: hr_db
SELECT *
FROM hr
LIMIT 10;


SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'hr';

--melihat rata' dan maksimum gaji
SELECT 
	gender,
	department,
	COUNT(employee_id) AS jumlah_karyawan,
	AVG(monthly_salary_idr) AS rata_rata_gaji,
	MAX(monthly_salary_idr) AS gaji_tertinggi
FROM hr
WHERE employee_status = 'Active'
GROUP BY department,gender
ORDER BY department,gender;

--menghitung loyalitas karyawan
SELECT 
	employee_id,
	department,
	hire_date,
	(2026 - EXTRACT(YEAR FROM hire_date)) AS lama_bekerja,
	CASE
		WHEN(2026 - EXTRACT(YEAR FROM hire_date)) < 1 THEN 'New Hire'
		WHEN(2026 - EXTRACT(YEAR FROM hire_date)) BETWEEN 1 AND 2 THEN 'Junior'
		WHEN(2026 - EXTRACT(YEAR FROM hire_date)) BETWEEN 3 AND 4 THEN 'Mid'
		ELSE 'Senior'
	END AS loyalitas_karyawan
FROM hr
WHERE employee_status = 'Active'
ORDER BY department;

--Menghitung persentase karyawan resigned
SELECT 
	department,
	COUNT(CASE WHEN employee_status ='Resigned' THEN 1 END) AS jumlah_karyawab_resign,
	COUNT(employee_id) AS total_karyawan,
	
	ROUND(
		(COUNT(CASE WHEN employee_status = 'Resigned' THEN 1 END)::NUMERIC / COUNT(employee_id)) * 100,2
	) AS presentase
FROM hr
GROUP BY department;